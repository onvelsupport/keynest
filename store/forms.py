from django import forms
from .models import Entry


class EntryForm(forms.ModelForm):

    agree = forms.BooleanField(
        required=True,
        label="I agree to the Terms & Conditions"
    )

    class Meta:
        model = Entry

        fields = [
            "full_name",
            "email",
            "phone",
            "postcode"
        ]