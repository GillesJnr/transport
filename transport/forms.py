from django import forms
from django.contrib.auth.models import User


class CreateLoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['email', 'password']