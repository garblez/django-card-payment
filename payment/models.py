from django.db import models

"""
When developing either User accounts or Customer, extend from this as a secondary
class and implement this class' members as model entries.
"""
class CardPayer():
    def __init__(self):
        self.email = None
        self.description = None
        self.card_token = None

    def set_description(self, description):
        self.description = description

    def set_card_token(self, card_token):
        self.card_token = card_token

    def set_email(self, email):
        self.email = email

# TODO add a paying user model for DB storage: User model for rest of project but also inheriting from CardPayer
