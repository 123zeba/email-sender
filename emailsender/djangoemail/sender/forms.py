from django import forms


class SubscribeForm(forms.Form):
    subject=forms.CharField()
    message=forms.CharField()
    email = forms.EmailField()