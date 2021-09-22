class Game:
    def __init__(self, name, designer, genre, production_year):
        self.name = name
        self.designer = designer
        self.genre = genre
        self.production_year = production_year

    def get_descriptive_name(self):
        long_name = f'{self.name} {self.designer} {self.genre} {self.production_year}'
        return long_name.title()