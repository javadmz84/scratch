from car import Car
from car import Battery

class ElectricCar(Car):
    def __init__(self, company, model, year):
        super().__init__(company, model, year)
        self.battery_size = 75
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kwh battery')

    def fill_gas_tank(self):
        print ("It doesn't need a gas tank")
my_elec = ElectricCar('BMV', 'IX', '2022')

print(my_elec.get_descriptive_name())
my_elec.describe_battery()
my_elec.fill_gas_tank()
