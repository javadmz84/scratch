from game import Game

class Specifications (Game):
    def __init__(self, name, designer, genre, production_year):
        super().__init__(name, designer, genre, production_year)

game2 = Specifications('God of war:2018' , 'Derek Daniels', 'Action_Adventure', '20 April 2018' )

print(game2.get_descriptive_name())