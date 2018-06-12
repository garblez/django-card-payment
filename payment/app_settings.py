from django.conf import settings


STRIPE_SECRET = getattr(settings, 'STRIPE_SECRET', '')
STRIPE_PUBLIC = getattr(settings, 'STRIPE_PUBLIC', '')
STRIPE_CURRENCY = getattr(settings, 'STRIPE_CURRENCY', 'USD')

