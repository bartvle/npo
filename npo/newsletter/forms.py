"""
"""


from django import forms

from .models import Subscription


error_messages = {
    'required': 'Dit is geen geldig e-mailadres',
    'invalid': 'Dit is geen geldig e-mailadres',
    'unique': 'Je bent al ingeschreven!',
    }


class NewsletterForm(forms.ModelForm):
    """
    """

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Vul hier je e-mailadres in', 'novalidate': ''}), error_messages=error_messages)

    class Meta:
        model = Subscription
        fields = ['email']
