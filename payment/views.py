from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Card

from datetime import datetime

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
        return render(request, 'payment/charge_card.html', {'request_email':True})

    def post(self, request, *args, **kwargs):

        try:
            charge = stripe.Charge.create(
                amount=data.context['amount'],
                currency=STRIPE_CURRENCY,
                api_key=STRIPE_SECRET,
                source=token,
                description=description
            )

            return HttpResponse("Charge succeeded")

        except Exception as e:
            return HttpResponse("Charge declined")
