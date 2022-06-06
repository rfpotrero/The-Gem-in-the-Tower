import random
import time
from tokenize import PseudoExtras
from functions import *
from colored import fg, bg, attr


title_colour_font = fg(69)
description_colour_font = fg(191)
floor_choice_colour = fg(214)
combat_colour_font = fg(125)
reset_font_style = attr(0)

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

def chance_of_encounter(odds_chance):
    """
    This will calculate the chance of encounter while
    the player search_floor or rest
    Credits to Daniel Poston for the main code
    https://www.datacamp.com/tutorial/statistics-python-tutorial-probability-1
    """
    event_outcome = random.randint(0,10)
    probability = event_outcome * 10
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
    P_S("The fight is over while your heartbeat still pound hard in your chest")
    P_S("you stop for a moment to consider your next move.")
    P_S("1- Continue moving ahead")
    P_S("2- Stop and healing")
    after_combat_choice = input("What you would do?")
    if after_combat_choice == "1":
        P_S("Not wasting any time you decided to move forward")
        P_S("The path to the next floors seems clear")
    elif after_combat_choice == "2":
        P_S("The adrenaline is fading away and the injuries from the last")
        P_S("The last fight are starting to hurt. You decided to stop before")
        P_S("they get worse.")
        P_S("While applying the bandages a sudden sound catch your attention..")
        if chance_of_encounter(100) is True:
            P_S("A see you from the distance and start to run towards you!")
            P_S("Get ready!")
            encounter(player_character)
        else:
            P_S("You hold your breath for a second but nothin happen")
            P_S("with the wounds bandage you resume your exploration")
            player_character.healing_up()
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

    Args:
        player_character (Class): This is the instance created in the main function. 
        It is the player and will be persistent until the end of the game.
    """
    P_S(description_colour_font + "Dust cover everything in the halls, market stall appear abandod")
    P_S("As if they all left in a rush")
    P_S("The halls might have something of value but be careful" + reset_font_style)
    P_S(floor_choice_colour+"What do you want to do?")
    P_S("1- Search and Prepare")
    P_S("2- Continue climbin the tower")
    first_floor_choice = input("" + reset_font_style)
    if first_floor_choice == "1":
        if chance_of_encounter(80) is True:
            P_S(description_colour_font + "While searching for anything of value the sound")
            P_S("a sudden cry pierced the silence and you turn just in")
            P_S("to see a strange creature charging!" + reset_font_style)
            P_S(combat_colour_font + "Get ready!"+ reset_font_style)
            encounter(player_character)
        else:
            P_S(description_colour_font + "You were ready to give up and complaint about wasting time")
            P_S("While a bright blade caught your eye a quick cleaning")
            P_S("Reveals an extraordinary weapon that will surely help")
            P_S("on what you will facing ahead." + reset_font_style)
            player_character.attack = player_character.attack + 2
    elif first_floor_choice == "2":
        if chance_of_encounter(50) is True:
            P_S( description_colour_font + "Moving forward you spot what looks like the stairs to")
            P_S("The next level. You are almost at the start of the stairs")
            P_S("When the clash and metal and stone draw you attention")
            P_S("A lonely creature is approaching...")
            P_S("Get ready!" + reset_font_style)
            encounter(player_character)
        else:
            P_S(description_colour_font + "Moving forward you spot what looks like the stairs to")
            P_S("The next level. You are almost at the start of the stairs")
            P_S("Climbing the startirs is easy, the worn stone under your feet")
            P_S("Is smooth. While walking you wondered what happened here.." + reset_font_style)
    else:
        print("You need to select a valid action")

def second_floor_action(player_character):
    """
    Second floor actions description and result.
    """
    P_S("Wandering through the dead city you spot the familiar sing of a smith")
    P_S("It is massive building the big forges now dark and dead but")
    P_S("you can easily imagine how busy this building and the sound of hammering")
    P_S("There might be some items left behind inside the massive building")
    P_S("it will make you take a detour and add a few hours...would it be worhty?")
    P_S("What you would?")
    P_S("")
    second_floor_choice = input(description_colour_font + """
    1- Enter the forge
    2- Whatever is there is not worthy
    """ + reset_font_style)
    if second_floor_choice == "1":
        if chance_of_encounter(80) is True:
            P_S(description_colour_font + "The makeshift torch hold the darkness at bay")
            P_S("hammers and anvil are starting to rust some still have the pieces")
            P_S("of steel over there as if waiting to be completed...")
            P_S("Suddenly your hair stand up on the back of your neck a pair")
            P_S("of eyes glow in the darkness getting closer..."+ reset_font_style)
            P_S(combat_colour_font + "Get Ready!" + reset_font_style)
            encounter(player_character)
        else:
            P_S(description_colour_font + "The makeshift torch hold the darkness at bay")
            P_S("hammers and anvil are starting to rust some still have the pieces")
            P_S("of steel over there as if waiting to be completed...")
            P_S("Suddenly your hair stand up on the back of your neck a pair")
            P_S("You turn with your weapon ready....")
            P_S("a quite laugh escape your lips. What looked like enemies is a row")
            P_S("of armour stands..getting closer this marvelous craft still is usable")
            P_S("You spot a shield the surface smooth and dusty but the straps are sturdy")
            P_S("and the metal strong. You take it with you, any help is welcome here" + reset_font_style)
            player_character.armour = player_character.armour + 2
    elif second_floor_choice == "2":
        P_S(description_colour_font + "You left the building behind an continue to move towards the main street")
        P_S("a wide avenue that in better time for sure would have been a breath taking sight")
        P_S("the street appears to converge in what looks like the access to upwards..." + reset_font_style)

def third_floor_action(player_character):
    """
    Third floor description
    """
    P_S(description_colour_font + "The glittering of jewels makes you stop in your heels, the riches in this")
    P_S("will be enough to live a life of comfort but that is not what you are here for" +  reset_font_style)
    P_S(floor_choice_colour + "What do you want to do?")
    P_S("""
        1- Enter and search
        2- That is not what I am here for!
        """ + reset_font_style)
    third_floor_choice = input("")
    if third_floor_choice == "1":
        if chance_of_encounter(80) is True:
            P_S(description_colour_font + "Your eyes can't believe the amount of diamonds, ruby and other")
            P_S("many precious stones in the same room. You are roaming day dreaming")
            P_S("about pack your bags with as many jewels and have a good life")
            P_S("your hand is almost reaching to an exquisite crown when")
            P_S("a gurgling noise raise from the end of the shop followed by a")
            P_S("create stumbling towards you" + reset_font_style)
            P_S(combat_colour_font + "Get ready!"  + reset_font_style)
            encounter(player_attack)
        else:
            P_S(description_colour_font + "Your eyes can't believe the amount of diamonds, ruby and other")
            P_S("many precious stones in the same room. You are roaming day dreaming")
            P_S("about pack your bags with as many jewels and have a good life.")
            P_S("Wandering the room you endup in front a display with a ring in the center")
            P_S("you can swear that the ring glows but is hard to tell you reach for")
            P_S("the ring. It feels warm and comforting in your hand. Suddenly the")
            P_S("the old and new injuries seems to hurt less.." + reset_font_style)
            player_character.hp = player_character.hp + 1
    else:
        P_S(description_colour_font + "You are no here for this! The final prize will make looks this like a cheap")
        P_S("glass and tin copy. Steeling yourself you push forward to the stair")
        P_S("leaving behind richeness beyong your wildest dreams" + reset_font_style)

def main():

    """
    Main Game function
    """
    player_character = Player()
    print( title_colour_font +
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
    """ + reset_font_style)

    while True:
        player_character.name = input(
            "Welcome to the tower what is your name adveturer?"
        )
        if player_character.name.isalpha():
            print(f"Very well {player_character.name} you are free to enter")
            break
        else:
            print("I am afraid do not understsand that. Can you say it again?")
    description_colour_font
    intro()
    first_floor()
    first_floor_action(player_character)
    second_floor()
    second_floor_action(player_character)
    thrid_floor()
    final_fight(player_character)


if __name__ == '__main__':
    main()
