class Animal:
    type= 'bird'
    def __init__(self, kind, color, longevity):
        self.kind = kind
        self.color = color
        self.longevity = longevity



    def fly(self):
        print(f'{self.kind} is flying now')

    def sit(self):
        print(f'{self.kind} is sitting on a tree now')

bird_1 = Animal('Eagle', 'black and white', 'about 20' )
bird_2 = Animal('Crow','black', 'about 10' )

print (bird_1.kind)
print (bird_1.color)
print (bird_1.longevity)
print (20*'*')
print (bird_2.kind)
print (bird_2.color)
print (bird_2.longevity)

bird_1.fly()
bird_2.sit()

