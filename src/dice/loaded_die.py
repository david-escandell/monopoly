from dice.die import Die

class LoadedDie(Die) :
    def __init__(self, numSides):
        self.numSides = numSides   

    def roll(self):
        return self.numSides