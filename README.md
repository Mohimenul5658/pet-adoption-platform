# 🐾 Pet Adoption & Rescue Platform

A Django-based Pet Adoption & Rescue Platform where users can browse available pets, search and filter pets, submit adoption requests, and manage their applications.

The project includes both a Django Template-based website and a REST API using Django REST Framework.

##  Features

###  User Features

- User Registration
- User Login
- User Logout
- User Profile
- Browse Available Pets
- Pet Details
- Search Pets
- Filter Pets
- Submit Adoption Requests
- View My Adoption Requests
- Adoption Request Status

### Pet Management

- Add Pet
- Edit Pet
- Delete Pet
- Upload Pet Image
- Pet Animal Type
- Breed
- Age
- Gender
- Location
- Description
- Adoption Status

### Search & Filtering

Users can search and filter pets by:

- Pet Name
- Animal Type
- Breed
- Gender
- Location
- Adoption Status

### Adoption System

Users can submit an adoption request for available pets.

An adoption request contains:

- Address
- Phone Number
- Reason for Adoption
- Previous Pet Experience
- Additional Message

### Business Logic

- Only available pets can receive adoption requests.
- A user cannot submit multiple active requests for the same pet.
- When an adoption request is approved, the pet automatically becomes Adopted.
- Adopted pets cannot receive new adoption requests.

### Django Admin

Administrators can:

- Manage Pets
- Manage Adoption Requests
- Change Pet Status
- Approve Adoption Requests
- Reject Adoption Requests

## REST API

### Pet API

```text
GET     /api/pets/
GET     /api/pets/<id>/
POST    /api/pets/
PUT     /api/pets/<id>/
DELETE  /api/pets/<id>/
```
### Adoption API
GET     /api/adoptions/
POST    /api/adoptions/
GET     /api/adoptions/<id>/
PUT     /api/adoptions/<id>/

### Token Authentication
POST /api/token/

### Search
GET /api/pets/?search=golden

### Filtering
GET /api/pets/?animal_type=Dog
GET /api/pets/?gender=Male
GET /api/pets/?status=Available

### Technologies Used
Python
Django
Django REST Framework
SQLite
HTML
CSS
Bootstrap
Token Authentication

### Installation
1. Clone the repository
  git clone https://github.com/Mohimenul5658/pet-adoption-platform
  cd pet-adoption-platform

2. Create virtual environment
  python -m venv venv

3. Activate virtual environment
  venv\Scripts\activate

4. Install dependencies
  pip install -r requirements.txt

5. Run migrations
  python manage.py migrate

6. Create superuser
  python manage.py createsuperuser

7. Run development server
  python manage.py runserver
  http://127.0.0.1:8000/
  http://127.0.0.1:8000/admin/

### Project Structure
pet-adoption-platform/
│
├── accounts/
├── adoptions/
├── pets/
├── config/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

## Author
Mohimenul Islam