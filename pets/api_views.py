from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from .models import Pet
from .serializers import PetSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "animal_type",
        "gender",
        "status",
    ]

    search_fields = [
        "name",
        "breed",
        "location",
        "description",
    ]

    ordering_fields = [
        "name",
        "age",
        "created_at",
    ]

    ordering = [
        "-created_at"
    ]
    
    permission_classes = [
    permissions.IsAuthenticatedOrReadOnly
]