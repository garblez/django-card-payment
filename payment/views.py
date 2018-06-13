from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from datetime import datetime


from payment.forms import VisitorEmailForm
from payment.models import Card

import stripe

from payment.app_settings import STRIPE_CURRENCY, STRIPE_SECRET

class SaveCard(View):
    @login_required
    def get(self, request, *args, **kwargs):
        pass

    @login_required
    def post(self, request, *args, **kwargs):
        pass


class ChargeCard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'payment/charge_card.html', {'amount': 500})

    def post(self, request, *args, **kwargs):


        if request.user.is_authenticated():
            email = request.user.email
            print email
        else:
            form = VisitorEmailForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['visitor_email']
                print email
            else:
                raise Exception("No contact email supplied")

        description = "[{0}]  Charge of {1}{2} made to account with email {3}".format(
            datetime.now(), request.POST['amount'], STRIPE_CURRENCY, email
        )

        try:
            token = request.POST.get('stripeToken', 'tok_invalidCard')
            print token

            charge = stripe.Charge.create(
                amount=request.POST['amount'],
                currency=STRIPE_CURRENCY,
                api_key=STRIPE_SECRET,
                source=token,
                description=description
            )

            return HttpResponse("Charge succeeded for "+ token )

        except Exception as e:
            return HttpResponse("Charge declined: "+e.message)
