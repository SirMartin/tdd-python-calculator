import random
import math
from random import randint
import sys

def generateSmallFloat():
    randomNumber = random.uniform(-1.00, 1.00)
    digits = list(str(randomNumber))
    return randomNumber, digits 

def generatePositiveInt():
    randomNumber = randint(0, 100)
    digits = list(str(randomNumber))
    return randomNumber,digits

def generatePositiveFloat():
    randomNumber = random.uniform(0.0, 100.0)
    digits = list(str(randomNumber))
    return randomNumber, digits

def generateNegativeInt():
    randomNumber = randint (-100, 0)
    digits = list(str(randomNumber))
    return randomNumber, digits

def generateNegativeFloat():
    randomNumber = random.uniform(-100.0, 0.0)
    digits = list(str(randomNumber))
    return randomNumber, digits

def generatePositiveToNegativeInt():
    randomNumber = randint(-100, 100)
    digits = list(str(randomNumber))
    return randomNumber, digits

def generatePositiveToNegativeFloat():
    randomNumber = random.uniform(-1000.0, 1000.0)
    digits = list(str(randomNumber))
    return randomNumber, digits

def generateLargeInt():
    randomNumber = randint(1000, 100000)
    digits = list(str(randomNumber))
    return randomNumber, digits

def generateNegativeLargeInt():   
    randomNumber = randint(-100000, 1000)
    digits = list(str(randomNumber))
    return randomNumber, digits

def generateVeryLargeInt():
    randomNumber = randint(10, 100)
    result = math.factorial(randomNumber)
    diigits = list(str(result))
    return result, diigits