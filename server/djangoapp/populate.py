from djangoapp.models import CarMake, CarModel


def populate_db():
    car_makes = [
        {'name': 'Toyota', 'description': 'Japanese car manufacturer'},
        {'name': 'Ford', 'description': 'American car manufacturer'},
        {'name': 'Honda', 'description': 'Japanese car manufacturer'},
        {'name': 'BMW', 'description': 'German car manufacturer'},
        {'name': 'Audi', 'description': 'German car manufacturer'},
        {'name': 'Mercedes', 'description': 'German car manufacturer'},
        {'name': 'Chevrolet', 'description': 'American car manufacturer'},
        {'name': 'Nissan', 'description': 'Japanese car manufacturer'}
    ]

    car_models = [
        {'name': 'Camry', 'car_make': 'Toyota', 'type': 'SEDAN',
         'year': 2023},
        {'name': 'Corolla', 'car_make': 'Toyota', 'type': 'SEDAN',
         'year': 2022},
        {'name': 'F-150', 'car_make': 'Ford', 'type': 'SUV',
         'year': 2021},
        {'name': 'Accord', 'car_make': 'Honda', 'type': 'SEDAN',
         'year': 2023},
        {'name': 'Civic', 'car_make': 'Honda', 'type': 'SEDAN',
         'year': 2022},
        {'name': 'X5', 'car_make': 'BMW', 'type': 'SUV',
         'year': 2021},
        {'name': 'Q5', 'car_make': 'Audi', 'type': 'SUV',
         'year': 2023},
        {'name': 'A4', 'car_make': 'Audi', 'type': 'SEDAN',
         'year': 2022},
        {'name': 'E-Class', 'car_make': 'Mercedes', 'type': 'SEDAN',
         'year': 2021},
        {'name': 'Malibu', 'car_make': 'Chevrolet', 'type': 'SEDAN',
         'year': 2023},
        {'name': 'Altima', 'car_make': 'Nissan', 'type': 'SEDAN',
         'year': 2022},
    ]

    for car_make in car_makes:
        CarMake.objects.create(
            name=car_make['name'],
            description=car_make['description']
        )

    for car_model in car_models:
        car_make = CarMake.objects.get(name=car_model['car_make'])
        CarModel.objects.create(
            name=car_model['name'],
            car_make=car_make,
            type=car_model['type'],
            year=car_model['year']
        )
