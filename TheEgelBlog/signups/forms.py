from django import forms

from .models import SignUp

class SingUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
