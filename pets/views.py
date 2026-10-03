from django.shortcuts import get_object_or_404, render

from .models import Pet


def home_view(request):
    pets = Pet.objects.filter(
        status=Pet.AdoptionStatus.AVAILABLE
    )[:6]

    return render(
        request,
        "home.html",
        {"pets": pets},
    )


def pet_list_view(request):
    pets = Pet.objects.all()

    search = request.GET.get("search", "").strip()
    animal_type = request.GET.get("animal_type", "").strip()
    breed = request.GET.get("breed", "").strip()
    gender = request.GET.get("gender", "").strip()
    location = request.GET.get("location", "").strip()
    status = request.GET.get("status", "").strip()

    if search:
        pets = pets.filter(name__icontains=search)

    if animal_type:
        pets = pets.filter(animal_type=animal_type)

    if breed:
        pets = pets.filter(breed__icontains=breed)

    if gender:
        pets = pets.filter(gender=gender)

    if location:
        pets = pets.filter(location__icontains=location)

    if status:
        pets = pets.filter(status=status)

    context = {
        "pets": pets,
        "search": search,
        "animal_type": animal_type,
        "breed": breed,
        "gender": gender,
        "location": location,
        "status": status,
        "animal_types": Pet.AnimalType.choices,
        "genders": Pet.Gender.choices,
        "statuses": Pet.AdoptionStatus.choices,
    }

    return render(
        request,
        "pets/pet_list.html",
        context,
    )


def pet_detail_view(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    return render(
        request,
        "pets/pet_detail.html",
        {"pet": pet},
    )
