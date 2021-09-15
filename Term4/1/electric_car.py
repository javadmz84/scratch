from car import Car

class ElectricCar(Car):
    def __init__(self, company, model, year):
        super().__init__(company, model, year)

my_elec = ElectricCar('BMV', 'IX', '2022')

print(my_elec.get_descriptive_name())