from django.urls import path

from . import views


urlpatterns = [
    path("", views.home_view, name="home"),

    path(
        "pets/",
        views.pet_list_view,
        name="pet_list",
    ),

    path(
        "pets/<int:pk>/",
        views.pet_detail_view,
        name="pet_detail",
    ),
]