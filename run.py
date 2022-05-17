# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pydoc import ModuleScanner
import random
import math
from re import M

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
        self.name = ""

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

def dice_roll(number_of_dices):
    """
    Generic functions to resolve any other roll dices
    """
    results =[]
    for dice in range(number_of_dices):
        roll = random.randint(1,6)
        results.append(roll)
    dice_result = sum[results]
    return dice_result

def encounter():
    """
    This is used to represent the fight with a monster and advance to the next tower's level
    """
    print("Fight Starts")
    monster_alive = True
    player_alive = True
    while monster_alive == True:
        player_attack = attack_roll(player1.attack)
        if player_attack  >= monster1.armour:
            print("The player hit the monster")
            monster1.hp = monster1.hp - 1
    
        else:
            print("The player attack failed")


def player_hit():
    """
    Fuction used to calculate if an injuried is inflicted
    """
    player_attack = attack_roll(player1.attack)
    if player_attack  >= monster1.armour:
        print("The player hit the monster")
        monster1.hp = monster1.hp - 1
    else:
        print("The player attack failed")
   

def monster_hit():
    """
    Fuction used to calculate if an injuried is inflicted
    """
    monster_attack = attack_roll(monster1.attack)
    if monster_attack  >= player1.armour:
        print("The monster hit the player")
        player1.hp = player1.hp - 1
    else:
        print("The monster attack failed")   

def main_game():
    """
    Main Game function
    """
    player_character = Player()
    while True:
        player_character.name = input("Welcome to the tower what is your name adveturer?")
        if player_character.name.isalpha():
            print(f"Very well {player_character.name} you are free to enter")
            break
        else:
            print("I am afraid do not understsand that. Can you say it again?")
