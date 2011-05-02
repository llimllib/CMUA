from django import forms

from cmua.registration.models import Register

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        exclude = ('last_modified', 'date_created', 'league')
