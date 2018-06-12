# Stripe Payment Django App
## Settings
Your Django project's settings.py must include options for your stripe
platform's STRIPE_PUBLIC and STRIPE_SECRET API keys alongside the
STRIPE_CURRENCY in use.

## Stripe card details entry form
This is put into the desired place of a given template by loading and calling the
appropriate template tag "card_entry". The card entry form itself has different
actions for saving card details and entering them directly and charging the
linked account.

## A note about HTTPS
Stripe will fail if you try to connect to it via HTTP. The standard Django
development server is also only capable of HTTP. In order to properly use this
app, the server it is run on must use HTTPS. For development of a project, one
can install django-secure and django-sslserver, set HTTPS/TLS settings to True
and manage.py runsslserver
