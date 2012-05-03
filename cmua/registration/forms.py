from django import forms

from cmua.registration.models import Register

class RegistrationForm(forms.ModelForm):
    def clean(self):
        monday = self.cleaned_data.get("monday_league")
        wednesday = self.cleaned_data.get("wednesday_league")

        errors = []
        if not monday and not wednesday:
            errors.append("You must select at least one league to play in")

        if not self.cleaned_data.get("i_agree_to_terms"):
            errors.append("You must agree to the terms of the waiver")

        if errors:
            raise forms.ValidationError(errors)

        return self.cleaned_data

    class Meta:
        model = Register
        exclude = ('last_modified', 'date_created', 'league')
