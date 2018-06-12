from django.shortcuts import render
from django.http import HttpResponse
from models import CardPayer

import stripe

#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required

from payment import app_settings


stripe.api_key = app_settings.STRIPE_SECRET


def test(request):
    return render(request, 'payment/test.html', {})

def charge(request):
    context_dict = {}

    if request.method == "POST":



        #  Try to charge the card represented by the stored/retrieved token.
        try:
            """
            This charge object when created tells the Stripe servers to charge an amount of pence to the customer
            credit/debit card with the given source token to be credited to the stripe platform with stripe.api_key
            Upon success, this will be recorded on the Stripe dashboard as a charge from source with a description
            and amount.
            """

            token = request.POST.get('stripeToken', 'tok_chargeDeclined')


            charge = stripe.Charge.create(
                amount=2000,
                currency='GBP',
                source="tok_visa_debit",
                description="Test charge visa debit",
                api_key=app_settings.STRIPE_PRIVATE
            )

            # We want to make sure that the card details stripe id is stored for future use in our database so we can
            # avoid card details being reentered in the future.
            # TODO: implement this feature for a customer account with card details taken from a profile settings page


        except stripe.error.CardError as ce:
            # The card didn't go through for whatever reason. Let the client know (DEBUG)
            return HttpResponse("Card error: " + ce.message)

        # Likewise a DEBUG statement
        return HttpResponse("Card payment worked for"+token)

    else:
        # Just save this new payment model anyway and present the form to input the details.

        return render(request, 'payment/charge.html', {})


def charge_card(request):
    return render(request, 'payment/charge.html', {'stripeToken':request.POST['stripeToken']})

def save_card(request):
    return render(request, 'payment/save.html', {'stripeToken': request.POST['stripeToken']})

def test_save(request):
    return render(request, 'payment/test.html', {'saving_card_details':True})