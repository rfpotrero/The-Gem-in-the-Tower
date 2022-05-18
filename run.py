# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pydoc import ModuleScanner
import random
import math
from re import M

from pydoc import ModuleScanner
import random
import math
from re import M


class Player:
    """
    This create an instance for the player
    """

    def __init__(self):
        hp = random.randint(1, 3)
        attack = random.randint(2, 3)
        initiative = random.randint(1, 6)
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

        hp = 1
        attack = random.randint(2, 3)
        initiative = random.randint(1, 6)
        self.hp = hp
        self.attack = attack
        self.initiative = initiative
        self.armour = 10

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

def attack_roll(number_of_dices):
    """
    This is used to generate the rolls for attacks.
    """
    results = []
    for dice in range(number_of_dices):
        roll = random.randint(1, 6)
        results.append(roll)
        attack_roll = sum(results)
    return attack_roll


def player_attack(player_raul, new_monster):
    """
    Fuction used to calculate if an injuried is inflicted
    """
    print("Player Attack!")
    player_attack = attack_roll(player_raul.attack)
    if player_attack >= new_monster.armour:
        print("The player hit the monster")
        new_monster.hp = new_monster.hp - 1
    else:
        print("The player attack failed")


def monster_attack(new_monster, player_character):
    """
    Fuction used to calculate if an injuried is inflicted
    """
    monster_attack = attack_roll(new_monster.attack)
    if monster_attack >= player_character.armour:
        print("The monster hit the player")
        player_character.hp = player_character.hp - 1
    else:
        print("The monster attack failed")


def main_function():

    """
    Main Game function
    """
    tower_floor = 0
    player_character = Player()
    while True:
        player_character.name = input(
            "Welcome to the tower what is your name adveturer?"
        )
        if player_character.name.isalpha():
            print(f"Very well {player_character.name} you are free to enter")
            break
        else:
            print("I am afraid do not understsand that. Can you say it again?")

    print("After climbing the stairs you arrive to the first floor")
    encounter(player_character)


def encounter(player_character):
    """
    This is used to represent the fight with a monster and advance to the next tower's level
    """
    new_monster = Monster()
    print("Fight Starts")
    monster_alive = True
    player_alive = True

    while monster_alive == True and player_alive == True:
        if player_character.initiative >= new_monster.initiative:
            print("The player go first")
            print("First loop player")
            player_action = input("""Selec your action:
            1- Attack
            2- Defend
            3- Heal
            """)
            if player_action == "1":
                player_attack(player_character, new_monster)
                if new_monster.hp == 0:
                    monster_alive = False
                    break
                print("The goblin is dead!")
            elif player_action == 2:
                print("PLayer defend")
                player_attack(player_character, new_monster)
                if new_monster.hp == 0:
                    monster_alive = False
                    break
            elif player_action == 3:
                print("player is healing up")
            else:
                print("That is not action you can do!")







            
            monster_attack(new_monster, player_character)
            if player_character.hp == 0:
                player_alive = False
                break
            print("The human is dead!")
        else:
            print("The monster go first")
            while monster_alive == True and player_alive == True:
                monster_attack(new_monster, player_character)
                if player_character.hp == 0:
                    player_alive = False
                    break
                print("The human is dead!")
                player_attack(player_character, new_monster)
                if new_monster.hp == 0:
                    monster_alive = False
                    break
                print("The goblin is dead!")


player_character = Player()

main_function()

