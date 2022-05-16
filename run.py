# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pydoc import ModuleScanner
import random
import math

print("This is the first stage")

class Player:
    """
    This create an instance for the player
    """
    def __init__(self):
        hp = random.randint(1,3)
        attack = random.randint(2,3)
        initiative  = random.randint(1,6)
        self.hp = hp
        self.attack = attack
        self.initiative = initiative
        self.armour = 12
        
        

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
        self.armour = 10
        

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
    print("The player attack!")
    player_hit()
    print("The monster attack!")    
    monster_hit()



def player_hit():
    """
    Fuction used to calculate if an injuried is inflicted
    """
    player_attack = attack_roll(player1.attack)
    if player_attack  >= monster1.armour:
        print("The player hit the monster")
        monster1.hp = monster1.hp - 1
    else:
        print("The attack failed")

def monster_hit():
    """
    Fuction used to calculate if an injuried is inflicted
    """
    monster_attack = attack_roll(monster1.attack)
    if monster_attack  >= player1.armour:
        print("The monster hit the player")
        player1.hp = player1.hp - 1
    else:
        print("The attack failed")    


monster1 = Monster()
player1 = Player()

encounter()
