class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        print(f'{self.model} changed color to {new_color}')
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        # constructor matching
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    counter = 0

    # constructor                    # parameters
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # fields / attributes
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

    # method
    def signal(self, number_of_times, sound):
        while number_of_times > 0:
            print(f'Car {self.model} is signalling - {sound}')
            number_of_times -= 1


class Truck(Car):
    counter = 0
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, weight, product_type):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg')
        else:
            print(f'You successfully loaded the cargo of {product_type} ({weight} kg)')


print('Start')
print(f'Factory CAR produced: {Car.counter} cars')

number = 65
bmw_car = Car('BMW X7', 2020, 'red')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} '
      f'COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

honda_car = Car('Honda Fit', 2009, 'blue', 5000)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} '
      f'COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}')
# honda_car.color = 'yellow'
honda_car.change_color('yellow')
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} '
      f'NEW COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}')

mers_car = Car(penalties=400, the_model='Mercedes 120',
               the_year=2017, the_color='silver')
print(f'MODEL: {mers_car.model} YEAR: {mers_car.year} '
      f'COLOR: {mers_car.color} PENALTIES: {mers_car.penalties}')

honda_car.drive('Osh')
bmw_car.drive('Kant')
mers_car.signal(5, 'Beep')
print(f'Factory CAR produced: {Car.counter} cars')

boeing_plane = Plane('Boeing 747', 2022, 'white')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} '
      f'COLOR: {boeing_plane.color}')

daf_truck = Truck('Daf 105', 2000, 'green',
                  900, 20000)

print(f'MODEL: {daf_truck.model} YEAR: {daf_truck.year} '
      f'COLOR: {daf_truck.color} PENALTIES: {daf_truck.penalties} '
      f'LOAD CAPACITY: {daf_truck.load_capacity}')
daf_truck.load_cargo( 25000, 'potatoes')
daf_truck.load_cargo( 15000, 'tomatoes')
daf_truck.drive('Tokmok')
print(f'Factory TRUCK produced: {Truck.counter} trucks')
print(f'Factory CAR produced: {Car.counter} cars')
print('End')