class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.company} {self.model}'
        return long_name.title()



my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()
