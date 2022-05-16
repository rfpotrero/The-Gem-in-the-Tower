# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pydoc import ModuleScanner
import random
import math

print("This is the first stage")

class Monster:
    """
    This create an instance of monster
    """
    def __init__(self):

        hp = random.randint(1,3)
        attack = random.randint(2,3)
        initiative  = random.randint(1,6)
        self.hp = hp
        self.attack = attack
        self.initiative = initiative
        

def chance_of_event():
    """
    This is used to generated an event
    """

def attack_roll(number_of_dices):
    """
    This is used to generate the rolls for attacks. 
    """
    results =[]
    for dice in range(number_of_dices):
        roll = random.randint(1,6)
        results.append(roll)
    attack_roll = sum(results)
    return attack_roll

def encounter():
    """
    This is used to represent the fight with a monster and advance to the next tower's level
    """

    print("A monster appear")


def fight():
    """
    Calculate the result of a fight
    """

