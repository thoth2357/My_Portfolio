from email.message import EmailMessage
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email= forms.EmailField(max_length=50, required=True)
    phone = forms.CharField(max_length=50, required=True)
    message = forms.CharField(widget=forms.Textarea)


