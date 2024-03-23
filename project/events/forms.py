from django import forms

from project.events.models import EventRegistration


class EventRegistrationForm(forms.ModelForm):
    confirm = forms.BooleanField(
        label="Confirm",
        widget=forms.CheckboxInput(),
        required=True,
    )

    class Meta:
        model = EventRegistration
        fields = ["confirm"]
