from django import forms

class ReceiptForm(forms.Form):
    image = forms.ImageField()

