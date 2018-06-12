# -*- coding: utf-8 -*-

from django import template
from payment import app_settings

SYMBOL = {
        'GBP': '£',
        'USD': '$',
        'EUR': '€',
        'JPY': '¥'
}

register = template.Library()


@register.inclusion_tag('payment/card_entry.html')
def card_entry_widget():
    return {}
