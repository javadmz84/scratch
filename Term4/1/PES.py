from game import Game

class Specifications (Game):
    def __init__(self, name, designer, genre, production_year):
        super().__init__(name, designer, genre, production_year)

game1 = Specifications('PES 2021' , 'Conami', 'Sport game', '15 september 2021' )

print(game1.get_descriptive_name())