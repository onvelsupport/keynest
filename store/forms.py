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
    "first_name",
    "last_name",
    "date_of_birth",
    "email",
    "phone",
    "address_line_1",
    "address_line_2",
    "city",
    "county",
    "postcode",
    "preferred_gift_card",
]

        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "address": forms.Textarea(attrs={"rows": 4}),
        }