from random import randrange

class Die:
    def roll(self):
        return randrange(self.numSides)+1