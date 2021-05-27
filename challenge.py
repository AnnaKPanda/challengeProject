# defining the Car class
class Car:
    # the constructor receives the following params: Years of release, KM, Name of car, Doors Open/Closed, the params should be sent as a tuple
    def __init__(self, *characteristics):
        self.year_of_release = characteristics[0]
        self.distance = characteristics[1]
        self.name = characteristics[2]
        self.door_status = characteristics[3]

    # method that calculates the insurance price according to Year of release and KM
    def calculate_insurance_price(self):
        if self.year_of_release < 2010 and self.distance > 8000:
            insurance_coef = 0.05
        elif self.year_of_release > 2010 and self.distance < 8000:
            insurance_coef = 0.07
        else:
            insurance_coef = 0.06
        insurance_price = self.year_of_release * insurance_coef
        print(f"{self.name}: {insurance_price}")

    # method that prints out the door status of the car
    def print_door_status(self):
        if self.door_status == True:
            door_status = 'open'
        else:
            door_status = 'closed'
        print(f'Car model is {self.name} and the doors status is {door_status}.')

    # method that prints out the car data
    def print_car_data(self):
        print(
            f'The car model is {self.name}, it was released at the year {self.year_of_release} and it passed {self.distance} km.')


ford_focus = Car(2012, 5000, 'Ford Focus', True)
audi_a3 = Car(1995, 80000, 'Audi A3', False)

print('Ford Focus data')
ford_focus.calculate_insurance_price()
ford_focus.print_door_status()
ford_focus.print_car_data()

print()
print('Audi A3 data')
audi_a3.calculate_insurance_price()
audi_a3.print_door_status()
audi_a3.print_car_data()



