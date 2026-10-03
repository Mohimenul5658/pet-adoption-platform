from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from pets.models import Pet

from .forms import AdoptionRequestForm
from .models import AdoptionRequest


@login_required
def adoption_create_view(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    if pet.status != Pet.AdoptionStatus.AVAILABLE:
        messages.error(
            request,
            "This pet has already been adopted."
        )
        return redirect("pet_detail", pk=pet.pk)

    existing_request = AdoptionRequest.objects.filter(
        user=request.user,
        pet=pet,
        status=AdoptionRequest.Status.PENDING,
    ).exists()

    if existing_request:
        messages.warning(
            request,
            "You already have a pending request for this pet."
        )
        return redirect("pet_detail", pk=pet.pk)

    if request.method == "POST":
        form = AdoptionRequestForm(
            request.POST,
            pet=pet,
            user=request.user,
        )

        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.user = request.user
            adoption_request.pet = pet
            adoption_request.save()

            messages.success(
                request,
                "Your adoption application has been submitted successfully."
            )

            return redirect("my_adoptions")

    else:
        form = AdoptionRequestForm(
            pet=pet,
            user=request.user,
        )

    return render(
        request,
        "adoptions/adoption_form.html",
        {
            "form": form,
            "pet": pet,
        },
    )


@login_required
def my_adoptions_view(request):
    adoption_requests = (
        AdoptionRequest.objects
        .filter(user=request.user)
        .select_related("pet")
    )

    return render(
        request,
        "adoptions/my_adoptions.html",
        {
            "adoption_requests": adoption_requests,
        },
    )
