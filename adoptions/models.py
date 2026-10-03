from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from pets.models import Pet


class AdoptionRequest(models.Model):

    class Status(models.TextChoices):
        PENDING = "Pending", "Pending"
        APPROVED = "Approved", "Approved"
        REJECTED = "Rejected", "Rejected"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="adoption_requests"
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="adoption_requests"
    )

    phone = models.CharField(max_length=20)

    address = models.TextField()

    reason = models.TextField()

    previous_pet_experience = models.BooleanField(default=False)

    message = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["user", "pet"],
                condition=models.Q(status="Pending"),
                name="unique_pending_adoption_request"
            )
        ]

    def clean(self):
        if not self.pet_id:
            return

        if self.pet.status == Pet.AdoptionStatus.ADOPTED:
            raise ValidationError(
            "This pet has already been adopted."
        )

        if self.status == self.Status.PENDING and self.user_id:
            existing_request = AdoptionRequest.objects.filter(
                user=self.user,
                pet=self.pet,
                status=self.Status.PENDING
            ).exclude(pk=self.pk).exists()

            if existing_request:
                raise ValidationError(
                    "You already have a pending request for this pet."
                )

    def save(self, *args, **kwargs):

        self.full_clean()

        if self.status == self.Status.APPROVED:
            self.pet.status = Pet.AdoptionStatus.ADOPTED
            self.pet.save(update_fields=["status"])

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.pet.name} - {self.status}"
