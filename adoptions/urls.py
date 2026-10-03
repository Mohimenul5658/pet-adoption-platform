from django.urls import path

from . import views


urlpatterns = [
    path(
        "apply/<int:pet_id>/",
        views.adoption_create_view,
        name="adoption_create",
    ),

    path(
        "my-requests/",
        views.my_adoptions_view,
        name="my_adoptions",
    ),
]