from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "animal_type",
        "breed",
        "age",
        "gender",
        "location",
        "status",
        "created_at",
    )

    list_filter = (
        "animal_type",
        "gender",
        "status",
        "location",
    )

    search_fields = (
        "name",
        "breed",
        "location",
        "description",
    )

    list_editable = ("status",)

    readonly_fields = ("created_at",)
