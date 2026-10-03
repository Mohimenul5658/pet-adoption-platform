from django.db import models


class Pet(models.Model):

    class AnimalType(models.TextChoices):
        DOG = "Dog", "Dog"
        CAT = "Cat", "Cat"
        BIRD = "Bird", "Bird"
        RABBIT = "Rabbit", "Rabbit"
        OTHER = "Other", "Other"

    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    class AdoptionStatus(models.TextChoices):
        AVAILABLE = "Available", "Available"
        ADOPTED = "Adopted", "Adopted"

    name = models.CharField(max_length=100)

    animal_type = models.CharField(
        max_length=20,
        choices=AnimalType.choices
    )

    breed = models.CharField(max_length=100)

    age = models.PositiveIntegerField(
        help_text="Age in years"
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )

    location = models.CharField(max_length=100)

    description = models.TextField()

    image = models.ImageField(
        upload_to="pets/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=AdoptionStatus.choices,
        default=AdoptionStatus.AVAILABLE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name