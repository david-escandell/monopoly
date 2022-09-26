import pytest

from src.dice.twelve_sided_die import TwelveSidedDie

def test_min():
    die = TwelveSidedDie()
    min = 1000
    numTimesToRoll = 10000

    for x in range(1, numTimesToRoll) :
        rolledValue = die.roll()
        if (rolledValue < min) :
            min = rolledValue
    assert min == 1

def test_max():
    die = TwelveSidedDie()
    max = 0
    numTimesToRoll = 10000

    for x in range(1, numTimesToRoll) :
        rolledValue = die.roll()
        if (rolledValue > max) : 
            max = rolledValue 
    assert max == 12

