import random
import time
from functions import *
from colored import fg, bg, attr

class Player:
    """
    This create an instance for the player
    """

    def __init__(self):
        hp = random.randint(1, 3)
        attack = random.randint(2, 3)
        # initiative = random.randint(1, 6)
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.initiative = 1
        self.armour = 12
        self.name = ""
    def healing_up(self):
        """
        Method to calculate healing
        """
        if self.max_hp == self.hp:
            print("You don't need to healyourself")
        else:
            self.hp = self.hp + 2
            print("You healed 2 hp")

class Monster:
    """
    This create an instance of monster
    """

    def __init__(self):

        hp = 1
        attack = random.randint(2, 3)
        # initiative = random.randint(1, 6)
        self.hp = hp
        self.attack = attack
        self.initiative = 2
        self.armour = 10

class FinalBoss:
    """
    This generate the final boss
    """
    def __init__(self):

        hp = 1
        attack = random.randint(2, 3)
        # initiative = random.randint(1, 6)
        self.hp = hp
        self.attack = attack
        self.initiative = 2
        self.armour = 10

def dice_roll(number_of_dices):
    """
    Generic functions to resolve any other roll dices
    """
    results = []
    for dice in range(number_of_dices):
        roll = random.randint(1, 6)
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
        attack_roll_dice = sum(results)
    return attack_roll_dice

def chance_of_encounter(even_outcome, sample_size, odds_chance):
    """
    This will calculate the chance of encounter while
    the player search_floor or rest
    Credits to Daniel Poston for the main code
    https://www.datacamp.com/tutorial/statistics-python-tutorial-probability-1
    """
    probability = (even_outcome / sample_size) * 100
    if probability  >= odds_chance:
        return True

def player_attack(player_character, new_monster):
    """
    Fuction used to calculate if an injuried is inflicted
    """
    print("Player Attack!")
    player_attack_roll = attack_roll(player_character.attack)
    if player_attack_roll >= new_monster.armour:
        print("The player hit the monster")
        new_monster.hp = new_monster.hp - 1
    else:
        print("The player attack failed")

def monster_attack(new_monster, player_character):
    """
    Fuction used to calculate if an injuried is inflicted
    """
    monster_attack_roll = attack_roll(new_monster.attack)
    if monster_attack_roll >= player_character.armour:
        print("The monster hit the player")
        player_character.hp = player_character.hp - 1
    else:
        print("The monster attack failed")

def after_combat(player_character):
    """
    This fuction provides information about of the combat.
    """
    P_S("What are you doing next?")
    P_S("1- Search and Prepare")
    P_S("2- Healing ")
    after_combat_choice = input("Choose careful!")
    if after_combat_choice == "1":
        if chance_of_encounter(50,100,50) is True:
            encounter(player_character)
        else:
            player_character.attack = player_character.attack + 2
    elif after_combat_choice == "2":
        if chance_of_encounter(50,100,50) is True:
            encounter(player_character)
    else:
        print("You need to select a valid action")

def game_over():
    """
    This function will end the current game when a player health_points
    reach zero and will ask the player if they want to play again.
    """
    P_S("The game is over")
    P_S("Do you have to play again?")
    game_over_option = input("""
    1- Play again
    2- Quit
    """)
    if game_over_option == "1":
        main()
    elif game_over_option == "2":
        exit()
    else:
        print("Please select a valid option")

def final_fight(player_character):
    """
    This will play the final boss fight
    """
    type_of_attack = ("powerful_attack", "fast_attack", "defend")

    boss_alive = True
    player_alive = True

    dragon = FinalBoss()
    print("You are face again the final boss of the tower")
    print("The dragon prepares to attack")
    while boss_alive is True and player_alive is True:
        boss_attack =  type_of_attack[random.randint(0, 2)]
        print(f"The dragon is preparing a {boss_attack} you what are you going to do!")
        player_choice =input(""" 1- Attack
        2- Defend 
        3- heal
        """)
        if boss_attack == "powerful_attack" and player_choice == "1":
            dragon.armour = dragon.armour  - 2
            print("You move faster at attack the dragon while preparing the attack")
            player_attack(player_character, dragon)
            if dragon.hp == 0:
                boss_alive = False
                print("The boss is dead!")
                break
            monster_attack(dragon, player_character)
            dragon.armour = dragon.armour + 2
            if player_character.hp == 0:
                player_alive = False
                print("The human is dead!")
                break
        elif boss_attack == "fast_attack" and player_choice == "2":
            print("You shield raised in a perfect block")
            dragon.attack = dragon.attack - 1
            monster_attack(dragon, player_character)
            if player_character.hp == 0:
                player_alive = False
                print("The human is dead!")
                break
            dragon.attack = dragon.attack + 1
            player_attack(player_character, dragon)
            if dragon.hp == 0:
                boss_alive = False
                print("The boss is dead!")
                break
        elif boss_attack == "defend":
            dragon.armour = dragon.armour + 2
            dragon.attack = dragon.attack - 2
            print("The dragon defend himself")
            player_attack(player_character, dragon)
            if dragon.hp == 0:
                boss_alive = False
                print("The boss is dead!")
                break
            monster_attack(dragon, player_character)
            if player_character.hp == 0:
                player_alive = False
                print("The human is dead!")
                break
            dragon.armour = dragon.armour - 2
            dragon.attack = dragon.attack + 2

        else:
            if boss_attack == "powerful_attack":
                dragon.attack = dragon.attack + 2
                player_attack(player_character, dragon)
                if dragon.hp == 0:
                    boss_alive = False
                    print("The boss is dead!")
                    break
                monster_attack(dragon, player_character)
                if player_character.hp == 0:
                    player_alive = False
                    print("The human is dead!")
                    break
                dragon.attack = dragon.attack - 2
            if boss_attack == "fast_attack":
                monster_attack(dragon, player_character)
                if player_character.hp == 0:
                    player_alive = False
                    print("The human is dead!")
                    break
                player_attack(player_character, dragon)
                if dragon.hp == 0:
                    boss_alive = False
                    print("The boss is dead!")
                    break

def encounter(player_character):
    """
    This is used to represent the fight with a monster and advance to the next tower's level
    """
    new_monster = Monster()
    print("Fight Starts")
    monster_alive = True
    player_alive = True

    if player_character.initiative >= new_monster.initiative:
        print("The player go first")
        while monster_alive is True and player_alive is True:
            player_action = input(
                """Selec your action:
                1- Attack
                2- Defend
                3- Heal
                """
            )
            if player_action == "1":
                player_attack(player_character, new_monster)
                if new_monster.hp == 0:
                    monster_alive = False
                    print("The goblin is dead!")
                    break
            elif player_action == "2":
                print("PLayer defend")
            elif player_action == "3":
                print("player is healing up")
            else:
                print("That is not action you can do!")

            if monster_alive is True:
                print("The monster attack!")
                monster_attack(new_monster, player_character)
                if player_character.hp == 0:
                    player_alive = False
                    game_over()

    else:
        print("The monster go first")
        while monster_alive is True and player_alive is True:
            print("The monster attack!")
            monster_attack(new_monster, player_character)
            if player_character.hp == 0:
                player_alive = False
                game_over()

            player_action = input(
                """Selec your action:
                1- Attack
                2- Defend
                3- Heal
                """
            )
            if player_action == "1":
                player_attack(player_character, new_monster)
                if new_monster.hp == 0:
                    monster_alive = False
                    print("The goblin is dead!")
                    break
            elif player_action == "2":
                print("PLayer defend")
            elif player_action == "3":
                print("player is healing up")
            else:
                print("That is not action you can do!")

def first_floor_action(player_character):
    """
    This fuctions will appear only in the first floor for the next floors
    the actions are different.
    """
    P_S("What are you doing next?")
    P_S("1- Search and Prepare")
    P_S("2- Continue climbin the tower")
    first_floor_choice = input("Choose careful!")
    if first_floor_choice == "1":
        if chance_of_encounter(50,100,50) is True:
            encounter(player_character)
        else:
            player_character.attack = player_character.attack + 2
    elif first_floor_choice == "2":
        if chance_of_encounter(50,100,50) is True:
            encounter(player_character)
    else:
        print("You need to select a valid action")

def main():

    """
    Main Game function
    """
    player_character = Player()
    print(
    """
_________          _______    _______  _______  _______   _________ _       
\__   __/|\     /|(  ____ \  (  ____ \(  ____ \(       )  \__   __/( (    /|
   ) (   | )   ( || (    \/  | (    \/| (    \/| () () |     ) (   |  \  ( |
   | |   | (___) || (__      | |      | (__    | || || |     | |   |   \ | |
   | |   |  ___  ||  __)     | | ____ |  __)   | |(_)| |     | |   | (\ \) |
   | |   | (   ) || (        | | \_  )| (      | |   | |     | |   | | \   |
   | |   | )   ( || (____/\  | (___) || (____/\| )   ( |  ___) (___| )  \  |
   )_(   |/     \|(_______/  (_______)(_______/|/     \|  \_______/|/    )_)
                                                                            
_________          _______   _________ _______           _______  _______ 
\__   __/|\     /|(  ____ \  \__   __/(  ___  )|\     /|(  ____ \(  ____ )
   ) (   | )   ( || (    \/     ) (   | (   ) || )   ( || (    \/| (    )|
   | |   | (___) || (__         | |   | |   | || | _ | || (__    | (____)|
   | |   |  ___  ||  __)        | |   | |   | || |( )| ||  __)   |     __)
   | |   | (   ) || (           | |   | |   | || || || || (      | (\ (   
   | |   | )   ( || (____/\     | |   | (___) || () () || (____/\| ) \ \__
   )_(   |/     \|(_______/     )_(   (_______)(_______)(_______/|/   \__/    
    """)

    while True:
        player_character.name = input(
            "Welcome to the tower what is your name adveturer?"
        )
        if player_character.name.isalpha():
            print(f"Very well {player_character.name} you are free to enter")
            break
        else:
            print("I am afraid do not understsand that. Can you say it again?")

    intro()
    first_floor()
    first_floor_action(player_character)
    second_floor()
    after_combat(player_character)
    thrid_floor()
    after_combat(player_character)
    final_fight(player_character)


if __name__ == '__main__':
    main()
