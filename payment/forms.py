from django import forms

class VisitorEmailForm(forms.Form):
    amount = forms.IntegerField()
    visitor_email = forms.CharField(max_length=256)