import pytest

from src.dice.four_sided_die import FourSidedDie

def test_min():
    die = FourSidedDie()
    min = 1000
    numTimesToRoll = 10000

    for x in range(1, numTimesToRoll) :
        rolledValue = die.roll()
        if (rolledValue < min) :
            min = rolledValue
    assert min == 1

def test_max():
    die = FourSidedDie()
    max = 0
    numTimesToRoll = 10000

    for x in range(1, numTimesToRoll) :
        rolledValue = die.roll()
        if (rolledValue > max) : 
            max = rolledValue 
    assert max == 4

