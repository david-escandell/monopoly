from dice.six_sided_die import SixSidedDie
import pytest

from src.dice.die_cup import DieCup
from src.dice.six_sided_die import SixSidedDie

def test_min():
    dieCup = DieCup([])
    dieCup.add(SixSidedDie())
    dieCup.add(SixSidedDie())
    min = 1000
    numTimesToRoll = 10000

    for x in range(1, numTimesToRoll) :
        rolledValue = dieCup.roll()
        if (rolledValue < min) :
            min = rolledValue
    assert min == 2

def test_max():
    dieCup = DieCup([])
    dieCup.add(SixSidedDie())
    dieCup.add(SixSidedDie())
    max = 0
    numTimesToRoll = 10000

    for x in range(1, numTimesToRoll) :
        rolledValue = dieCup.roll()
        if (rolledValue > max) : 
            max = rolledValue 
    assert max == 12

def test_add():
    dieCup = DieCup([])
    testDie = SixSidedDie()
    dieCup.add(testDie)
    assert testDie in dieCup.dice

def test_remove():
    dieCup = DieCup([])
    testDie = SixSidedDie()
    dieCup.add(testDie)
    dieCup.remove(testDie)

    assert testDie not in dieCup.dice