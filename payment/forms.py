from django import forms

class VisitorEmailForm(forms.Form):
    visitor_email = forms.CharField(max_length=256)