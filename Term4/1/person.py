class Person:
    def __init__(self, name, last_name, age, grade):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.grade = grade

    def get_descriptive_name(self):
        long_name = f'{self.name} {self.last_name} {self.age} {self.grade}'
        return long_name.title()
