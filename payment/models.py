from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

import stripe

from payment.app_settings import STRIPE_CURRENCY, STRIPE_SECRET

class Card(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def charge(self, amount):
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency=STRIPE_CURRENCY,
                api_key=STRIPE_SECRET,
                source=self.card_token,
                description="[{0}]   Payment of {1}GBP made by {2}".format(
                    datetime.now(), amount, self.email
                )
            )

        except Exception as e:
            print "An error occurred. Payment was declined."