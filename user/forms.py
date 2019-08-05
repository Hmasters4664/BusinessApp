from user.models import User
from django import forms
from django.forms import ModelForm


class UserAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')