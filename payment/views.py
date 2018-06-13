from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from models import Card

from datetime import datetime

import stripe

from payment.app_settings import STRIPE_CURRENCY, STRIPE_SECRET

class SaveCard(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class ChargeCard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'payment/charge_card.html', {'amount':5000})

    def post(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated() and Card.objects.get(user=request.user).token != '':
            card.charge(request.POST.amount)

        # In either case (logged in as authenticated user without saved payment method or logged out), the card entry
        # form was displayed so take the token from that and charge the card.

        data = request.POST
        token = data.POST.get('stripeToken', 'tok_chargeDeclined')
        description = "[{0}]    Payment of {1}GBP by {2}".format(
            datetime.now(),
            data.context['amount'],
            request.user.email if request.user and request.user.is_authenticated() else data.given_email
        )
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
