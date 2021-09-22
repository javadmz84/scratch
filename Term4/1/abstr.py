from abc import ABC, abstractmethod
class Aminity(ABC):
    def turn_on(self):
        print

class Electricity(Aminity):
    def turn_on(self):
        print("You flipped the light switch!")

class Water(Aminity):
    def turn_on(self):
        print("You pressed the faucet up!")

class Gas(Aminity):
    def turn_on(self):
        print("You turned the knob on the stovefront!")


E = Electricity()
E.turn_on()
W = Water()
W.turn_on()
G= Gas()
G.turn_on()