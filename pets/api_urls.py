from rest_framework.routers import DefaultRouter

from .api_views import PetViewSet


router = DefaultRouter()

router.register(
    "pets",
    PetViewSet,
    basename="pet",
)

urlpatterns = router.urls