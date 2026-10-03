from django import forms

from .models import AdoptionRequest


class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = [
            "address",
            "phone",
            "reason",
            "previous_pet_experience",
            "message",
        ]

        widgets = {
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter your full address",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your phone number",
                }
            ),
            "reason": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Why do you want to adopt this pet?",
                }
            ),
            "previous_pet_experience": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Additional message (optional)",
                }
            ),
        }

    def __init__(self, *args, pet=None, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.pet = pet
        self.user = user

        self.fields["previous_pet_experience"].label = (
            "Have you owned a pet before?"
        )

        self.fields["previous_pet_experience"].widget = forms.Select(
            choices=[
                (False, "No"),
                (True, "Yes"),
            ],
            attrs={
                "class": "form-select",
            },
        )

    def clean(self):
        cleaned_data = super().clean()

        if not self.pet:
            raise forms.ValidationError(
                "Invalid pet."
            )

        if self.pet.status != self.pet.AdoptionStatus.AVAILABLE:
            raise forms.ValidationError(
                "This pet has already been adopted."
            )

        if self.user:
            existing_request = AdoptionRequest.objects.filter(
                user=self.user,
                pet=self.pet,
                status=AdoptionRequest.Status.PENDING,
            ).exists()

            if existing_request:
                raise forms.ValidationError(
                    "You already have a pending request for this pet."
                )

        return cleaned_data