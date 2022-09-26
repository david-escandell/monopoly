from dice.die_cup import DieCup
from dice.loaded_die import LoadedDie
from dice.two_sided_die import TwoSidedDie
from dice.four_sided_die import FourSidedDie
from dice.six_sided_die import SixSidedDie
from dice.eight_sided_die import EightSidedDie
from dice.ten_sided_die import TenSidedDie
from dice.twelve_sided_die import TwelveSidedDie
from dice.twenty_sided_die import TwentySidedDie
from dice.one_hundred_sided_die import OneHundredSidedDie

def rollDie(die):
    # Roll 1000 times, get min and max and average
    numTimesToRoll = 10001
    min = numTimesToRoll
    max = 0
    sum = 0
    for x in range(1, numTimesToRoll) :
        rolledValue = die.roll()
        sum += rolledValue
        if (rolledValue < min) :
            min = rolledValue
        if (rolledValue > max) : 
            max = rolledValue 
    avg = sum // numTimesToRoll
    print("die ", type(die),"min: ", min, "max: ", max, " avg: ", avg)

rollDie(LoadedDie(100))
rollDie(TwoSidedDie())
rollDie(FourSidedDie())
rollDie(SixSidedDie())
rollDie(EightSidedDie())
rollDie(TenSidedDie())
rollDie(TwelveSidedDie())
rollDie(TwentySidedDie())
rollDie(OneHundredSidedDie())
rollDie(DieCup([SixSidedDie(), SixSidedDie()]))