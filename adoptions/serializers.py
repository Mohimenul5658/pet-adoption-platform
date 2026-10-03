from rest_framework import serializers

from pets.models import Pet

from .models import AdoptionRequest


class AdoptionRequestSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(
        source="user.username"
    )

    pet_name = serializers.ReadOnlyField(
        source="pet.name"
    )

    class Meta:
        model = AdoptionRequest

        fields = [
            "id",
            "user",
            "pet",
            "pet_name",
            "phone",
            "address",
            "reason",
            "previous_pet_experience",
            "message",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "pet_name",
            "created_at",
        ]

    def validate(self, attrs):
        request = self.context.get("request")
        pet = attrs.get("pet")

        # On update, use existing pet if pet wasn't sent
        if pet is None and self.instance:
            pet = self.instance.pet

        if pet is None:
            raise serializers.ValidationError({
                "pet": "Pet is required."
            })

        # New request / changing pet
        if pet.status == Pet.AdoptionStatus.ADOPTED:
            raise serializers.ValidationError({
                "pet": "This pet has already been adopted."
            })

        # Prevent duplicate pending requests
        if request and request.user.is_authenticated:
            existing = AdoptionRequest.objects.filter(
                user=request.user,
                pet=pet,
                status=AdoptionRequest.Status.PENDING,
            )

            if self.instance:
                existing = existing.exclude(
                    pk=self.instance.pk
                )

            if existing.exists():
                raise serializers.ValidationError({
                    "pet": "You already have a pending request for this pet."
                })

        return attrs

    def validate_status(self, value):
        request = self.context.get("request")

        # Only staff/admin can change status through API
        if request and not request.user.is_staff:
            if self.instance and value != self.instance.status:
                raise serializers.ValidationError(
                    "Only admin users can change adoption status."
                )

        return value

    def create(self, validated_data):
        request = self.context["request"]

        validated_data["user"] = request.user

        return super().create(validated_data)