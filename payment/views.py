from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from datetime import datetime


from payment.forms import VisitorEmailForm
from payment.models import Card
from payment.app_settings import STRIPE_CURRENCY, STRIPE_PRIVATE, STRIPE_PUBLIC

import stripe



class SaveCard(View):
    template = "payment/save_card.html"

    @login_required
    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})

    @login_required
    def post(self, request, *args, **kwargs):
        pass


class ChargeCard(View):
    template = "payment/charge_card.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {'amount': 500, 'currency': STRIPE_CURRENCY})

    def post(self, request, *args, **kwargs):
        print STRIPE_PRIVATE, STRIPE_CURRENCY, STRIPE_PUBLIC
        stripe.api_key = STRIPE_PRIVATE

        form = VisitorEmailForm(request.POST)
        if not form.is_valid():
            raise Exception("Invalid submission form.")  # DEBUG

        amount = form.cleaned_data['amount']
        email = form.cleaned_data['visitor_email']

        if request.user.is_authenticated():
            email = request.user.email

        description = "[{0}]  Charge of {1}{2} made to account with email {3}".format(
            datetime.now(),
            amount,
            STRIPE_CURRENCY,
            email
        )


        try:
            token = request.POST.get('stripeToken')
            print token

            charge = stripe.Charge.create(
                amount=amount,
                currency=STRIPE_CURRENCY,
                source=token,
                description=description
            )

            return HttpResponse("Charge succeeded for "+ token )
        except stripe.error.CardError:
            # Since the card was declined, stripe.error.CardError will be captured
            pass
        except stripe.error.RateLimitError as e:
            # Too many requests sent to Stripe within a short time frame.
            pass
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were given to Stripe
            pass
        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed (possible change in API keys)
            pass
        except stripe.error.APIConnectionError as e:
            # Failed to connect to Stripe
            pass
        except stripe.error.StripeError as e:
            # Generic Stripe card submission error: display an error to the user, email technical support.
            pass
        except Exception as e:
            return HttpResponse("Charge declined: "+e.message)
