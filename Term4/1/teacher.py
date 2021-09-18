from person import Person

class Specifications (Person):
    def __init__(self, name, last_name, age, grade):
        super().__init__(name, last_name, age, grade)

teacher1 = Specifications('Payam', 'Bahrampoor', '27', '10')

print(teacher1.get_descriptive_name())