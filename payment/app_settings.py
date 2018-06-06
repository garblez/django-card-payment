from django.conf import settings

STRIPE = getattr(settings, 'PAYMENT_STRIPE', [
    ('PUBLIC', ""),
    ('SECRET', ""),
    ('CURRENCY', "USD")
])
