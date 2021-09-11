class Student:
    type = 'Baharestan'
    def __init__(self, name, age, school, lastname):
        self.name = name
        self.age = age
        self.school = school
        self.lastname = lastname

    def eat(self):
        print(f'{self.name} is eating now')
    
    def playing(self):
        print(f'{self.name} is playing soccer now')

Student_1 = Student('Hossein', 16, 'Baharestan', 'Rezae')
Student_2 = Student('Reza', 17, 'Saheb al zaman', 'amirzadeh')


print(Student_1.age)
print(Student_1.name)
print(Student_1.lastname)
print(Student_1.school)
print (20*'*')
print(Student_2.age)
print(Student_2.name)
print(Student_2.lastname)
print(Student_2.school)

Student_1.eat()
Student_2.playing()