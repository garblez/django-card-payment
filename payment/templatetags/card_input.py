# -*- coding: utf-8 -*-

from django import template
from payment import settings

SYMBOL = {
        'GBP': '£',
        'USD': '$',
        'EUR': '€',
        'JPY': '¥'
}

register = template.Library()


@register.inclusion_tag('card_entry.html')
def card_entry_widget():
    return {}
