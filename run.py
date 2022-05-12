# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import math

print("This is the first stage")

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

def fight():
    """
    Calculate the result of a fight
    """
print(attack_roll(3))