from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel

# Get an instance of a logger
logger = logging.getLogger(__name__)

def initiate():
    # Example data to populate the database
    car_makes = [
        {'name': 'Toyota', 'description': 'Japanese car manufacturer'},
        {'name': 'Ford', 'description': 'American car manufacturer'},
    ]

    car_models = [
        {'name': 'Camry', 'car_make': 'Toyota', 'type': 'SEDAN', 'year': 2023},
        {'name': 'Corolla', 'car_make': 'Toyota', 'type': 'SEDAN', 'year': 2022},
        {'name': 'F-150', 'car_make': 'Ford', 'type': 'SUV', 'year': 2021},
    ]

    for car_make in car_makes:
        CarMake.objects.create(name=car_make['name'], description=car_make['description'])

    for car_model in car_models:
        car_make = CarMake.objects.get(name=car_model['car_make'])
        CarModel.objects.create(
            name=car_model['name'],
            car_make=car_make,
            type=car_model['type'],
            year=car_model['year']
        )

# Create your views here.
def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if count == 0:
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})
    return JsonResponse({"CarModels": cars})

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    data = {"userName": ""}
    return JsonResponse(data)

# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    context = {}
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False
    try:
        User.objects.get(username=username)
        username_exist = True
    except:
        logger.debug("{} is new user".format(username))
    if not username_exist:
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
        return JsonResponse(data)
    else:
        data = {"userName": username, "error": "Already Registered"}
        return JsonResponse(data)
