class DieCup() :
    def __init__(self, dice):
        self.dice = dice  

    def add(self, die):
        self.dice.append(die)

    def remove(self, die):
        self.dice.remove(die)

    def roll(self):
        total = 0
        for die in self.dice:
            total += die.roll()
        return total