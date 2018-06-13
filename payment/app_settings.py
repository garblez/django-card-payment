from django.conf import settings


STRIPE_PRIVATE = getattr(settings, 'STRIPE_PRIVATE', '')
STRIPE_PUBLIC = getattr(settings, 'STRIPE_PUBLIC', '')
STRIPE_CURRENCY = getattr(settings, 'STRIPE_CURRENCY', 'USD')

