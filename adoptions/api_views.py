from rest_framework import permissions, viewsets

from .models import AdoptionRequest
from .serializers import AdoptionRequestSerializer


class AdoptionRequestViewSet(viewsets.ModelViewSet):

    serializer_class = AdoptionRequestSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return AdoptionRequest.objects.none()

        if user.is_staff:
            return (
                AdoptionRequest.objects
                .select_related("user", "pet")
                .all()
            )

        return (
            AdoptionRequest.objects
            .select_related("user", "pet")
            .filter(user=user)
        )

    def get_permissions(self):
        return [
            permissions.IsAuthenticated()
        ]