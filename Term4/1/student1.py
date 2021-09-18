from person import Person

class Specifications (Person):
    def __init__(self, name, last_name, age, grade):
        super().__init__(name, last_name, age, grade)

Student1 = Specifications('Javad', 'Momenzadeh', '17', '10')

print(Student1.get_descriptive_name())