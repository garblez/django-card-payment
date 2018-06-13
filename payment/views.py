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
    @login_required
    def get(self, request, *args, **kwargs):
        pass

    @login_required
    def post(self, request, *args, **kwargs):
        pass


class ChargeCard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'payment/charge_card.html', {'amount': 500, 'currency': STRIPE_CURRENCY})

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

        except Exception as e:
            return HttpResponse("Charge declined: "+e.message)
