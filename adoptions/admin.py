from django.contrib import admin
from .models import AdoptionRequest


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "pet",
        "phone",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "pet__name",
        "phone",
        "address",
        "reason",
    )

    readonly_fields = (
        "user",
        "pet",
        "phone",
        "address",
        "reason",
        "previous_pet_experience",
        "message",
        "created_at",
    )

    list_editable = ("status",)

    ordering = ("-created_at",)