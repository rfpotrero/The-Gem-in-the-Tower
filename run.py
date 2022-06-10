"""
Module execute the game
"""
import random
from colored import fg, attr
from functions import (
    P_S,
    intro,
    first_floor,
    second_floor,
    thrid_floor,
    final_fight_description,
    player_final_fight_victory,
    player_death,
    game_ending_description,
)

title_colour_font = fg(69)
description_colour_font= fg(191)
description_colour_font_2 = fg(193)
floor_choice_colour = fg(214)
combat_colour_font = fg(124)
reset_font_style = attr(0)


class Player:
    """
    This create an instance for the player
    """

    def __init__(self):
        health_points = random.randint(2, 3)
        self.health_points = health_points
        self.max_health_points = health_points
        self.attack = 3
        self.armour = 12
        self.name = ""

    def healing_up(self):
        """
        Method to calculate healing
        """
        if self.max_health_points == self.health_points:
            print(
                combat_colour_font + "You don't need to healyourself" + reset_font_style
            )
        else:
            self.health_points = self.max_health_points
            print(
                combat_colour_font + "The potion heals your wounds!" + reset_font_style
            )

    def character_attack(self, other_oponent):
        """
        Fuction used to calculate if an injuried is inflicted
        """
        character_attack_roll = attack_roll(self.attack)
        if character_attack_roll >= other_oponent.armour:
            print(
                combat_colour_font
                + f"The attack was successful! {character_attack_roll}"
                + reset_font_style
            )
            other_oponent.health_points = other_oponent.health_points - 1
        else:
            print(
                combat_colour_font
                + f"The attack failed {character_attack_roll}"
                + reset_font_style
            )


def attack_roll(number_of_dices):
    """
    This is used to generate the rolls for attacks.

    Args:
        number_of_dices(int): This is the number of dices that a character will use
        to attack.

    Returns:
        attack_roll_result(int): This is the sum of the number of dices
    """
    attack_roll_result = 0
    for dice in range(number_of_dices):
        roll = random.randint(1, 6)
        attack_roll_result += roll
    return attack_roll_result


def encounter(player_character):
    """
    This is used to represent the fight with a monster and advance to the next tower's level

    Args:
        player_character (Class): This is the player character class generated in main()
    """

    new_monster = Player()
    new_monster.armour = new_monster.armour - 2

    monster_alive = True
    player_alive = True

    P_S(
        combat_colour_font
        + "You move weapon in had ready to face whatever this cursed place throw at you!"
        + reset_font_style
    )
    while monster_alive is True and player_alive is True:
        while True:
            player_action = input(
                combat_colour_font
                + """Select your action:
            1- Attack
            2- Defend
            3- Heal
            """
                + reset_font_style
            )
            if player_action == "1":
                player_character.character_attack(new_monster)
                if new_monster.health_points == 0:
                    monster_alive = False
                    P_S(
                        combat_colour_font
                        + "With a swift strike the monster falls blood spurting"
                        + reset_font_style
                    )
                    after_combat(player_character)
                    break
                P_S(combat_colour_font + "The monster attacks!" + reset_font_style)
                new_monster.character_attack(player_character)
                player_alive_check(player_character)
            elif player_action == "2":
                P_S(
                    combat_colour_font
                    + "You focus on avoiding or blocking attacks, riposting when the chance appears"
                    + reset_font_style
                )
                player_character.armour = player_character.armour + 2
                player_character.attack = player_character.attack - 1
                player_character.character_attack(new_monster)
                if new_monster.health_points == 0:
                    monster_alive = False
                    P_S(
                        combat_colour_font
                        + "With a swift strike the monster falls blood spurting"
                        + reset_font_style
                    )
                    after_combat(player_character)
                    break
                P_S(combat_colour_font + "The monster attacks!" + reset_font_style)
                new_monster.character_attack(player_character)
                player_alive_check(player_character)
                player_character.armour = player_character.armour - 2
                player_character.attack = player_character.attack + 1
            elif player_action == "3":
                P_S(
                    combat_colour_font
                    + "Reaching to your pouch you gulp down the red potion"
                    + reset_font_style
                )
                player_character.healing_up()
                new_monster.character_attack(player_character)
                player_alive_check(player_character)
            else:
                continue


def player_alive_check(player_character):
    """
    Check if the player is still above zero health points after a monster attack

    Args:
        player_character (Class): This is the player character class generated in main()
    """
    if player_character.health_points == 0:
        player_death()
        game_over()

def final_boss_alive_check(abomination):
    """
    Check if the final boss is still above zero health points after a player's attack

    Args:
        abomination (Class): This is generated in final_fight() and the represent the last boss
    """
    if abomination.health_points == 0:
        player_final_fight_victory()
        play_again()

def chance_of_encounter(odds_chance):
    """
    This will calculate the chance of encounter while
    the player search_floor or rest
    Credits to Daniel Poston for the main code
    https://www.datacamp.com/tutorial/statistics-python-tutorial-probability-1

    Args:
        odds_chance (int): This represent the chance of an action to success
    Returns:
        odds_chance (bool): Returns true if the actions is a success
    """
    event_outcome = random.randint(0, 10)
    probability = event_outcome * 10
    if probability <= odds_chance:
        return True

def after_combat(player_character):
    """
    This function provides information about of the combat.

    Args:
        player_character (Class): This is the player character class generated in main()
    """
    P_S(
        floor_choice_colour
        + "The fight is over, your heartbeat still pound hard in your chest"
    )
    P_S("you stop for a moment to consider your next move.")
    P_S("What do you want to do?")
    after_combat_choice = input(
        """
    1- Continue moving ahead
    2- Take a break and heal
    """
        + reset_font_style
    )
    if after_combat_choice == "1":
        P_S(
            description_colour_font_2 + "Not wasting any time you decided to move forward"
        )
        P_S("The path to the next floor seems clear")
        P_S("" + reset_font_style)
    elif after_combat_choice == "2":
        while True:
            if player_character.max_health_points > player_character.health_points:
                P_S(
                    description_colour_font_2
                    + "The adrenaline is fading and the injuries from the last"
                )
                P_S("fight are starting to hurt. You decided to stop before")
                P_S("they get worse.")
                P_S(
                    "While applying the bandages a sudden sound catch your attention.."
                    + reset_font_style
                )
                if chance_of_encounter(40) is True:
                    P_S(
                        description_colour_font
                        + "A monster starts to run towards you!"
                        + reset_font_style
                    )
                    P_S(combat_colour_font + "Get ready!" + reset_font_style)
                    player_character.healing_up()
                    encounter(player_character)
                    break
                else:
                    P_S(
                        description_colour_font_2
                        + "You hold your breath for a second but nothing happen"
                    )
                    P_S(
                        "with the wounds bandage you resume your exploration"
                        + reset_font_style
                    )
                    player_character.healing_up()
                    break
            P_S(
                description_colour_font_2
                + "After a quick check you don't find any injury and keep moving ahead"
                + reset_font_style
            )
            break

        else:
            print("You need to select a valid action")

def play_again():
    """
    Presents the user with the option to play again.

    """
    while True:
        P_S(description_colour_font + "Do you want to play again?")
        game_over_option = input(
            """
        1- Play again
        2- Quit
        """
            + reset_font_style
        )
        if game_over_option == "1":
            P_S("")
            main()
        elif game_over_option == "2":
            P_S(description_colour_font_2+ "Thanks for playing! Goodbye!" + reset_font_style)
            exit()
        else:
            continue

def game_over():
    """
    This function will end the current game when a player health_points
    reach zero and will ask the player if they want to play again.
    """
    P_S(description_colour_font + "You have died.")
    play_again()

def final_fight(player_character):
    """
    This generates the final boss fight.

    Args:
        player_character (Class): This is the player character class generated in main()
    """
    type_of_attack = ("powerful attack", "fast attack", "defend")

    boss_alive = True
    player_alive = True

    abomination = Player()

    final_fight_description()

    P_S(combat_colour_font + "The abomination moves towards you!")
    while boss_alive is True and player_alive is True:
        boss_attack = type_of_attack[random.randint(0, 2)]
        P_S(
            combat_colour_font
            + f"The abomination is preparing a {boss_attack} you what are you going to do!"
        )
        player_choice = input(
            """
        1- Attack
        2- Defend
        3- Heal
        """
            + reset_font_style
        )
        if boss_attack == "powerful attack" and player_choice == "1":
            abomination.armour = abomination.armour - 2
            P_S(
                combat_colour_font
                + "You move before the abomination and attack!"
                + reset_font_style
            )
            player_character.character_attack(abomination)
            final_boss_alive_check(abomination)
            P_S( combat_colour_font + "The abomination attack!" + reset_font_style)
            abomination.character_attack(player_character)
            abomination.armour = abomination.armour + 2
            player_alive_check(player_character)
        elif boss_attack == "fast attack" and player_choice == "2":
            P_S(
                combat_colour_font
                + "You shield raised in a perfect block"
                + reset_font_style
            )
            abomination.attack = abomination.attack - 1
            P_S( combat_colour_font + "The abomination attack!" + reset_font_style)
            abomination.character_attack(player_character)
            player_alive_check(player_character)
            abomination.attack = abomination.attack + 1
            P_S( combat_colour_font + "You attack!" + reset_font_style)
            player_character.character_attack(abomination)
            final_boss_alive_check(abomination)
        elif boss_attack == "defend":
            abomination.armour = abomination.armour + 2
            P_S(combat_colour_font + "The abomination is retreating!" + reset_font_style)
            P_S( combat_colour_font + "You attack!" + reset_font_style)
            player_character.character_attack(abomination)
            final_boss_alive_check(abomination)
            P_S( combat_colour_font + "The abomination attack!" + reset_font_style)
            abomination.character_attack(player_character)
            player_alive_check(player_character)
            abomination.armour = abomination.armour - 2
            abomination.attack = abomination.attack + 2
        elif player_choice == "3":
            P_S(combat_colour_font + "The abomination is retreating!" + reset_font_style)
            abomination.character_attack(player_character)
            player_character.healing_up()
        else:
            if boss_attack == "powerful attack":
                abomination.attack = abomination.attack + 2
                P_S( combat_colour_font + "You attack!" + reset_font_style)
                player_character.character_attack(abomination)
                final_boss_alive_check(abomination)
                P_S(combat_colour_font + "The abomination is retreating!" + reset_font_style)
                abomination.character_attack(player_character)
                player_alive_check(player_character)
                abomination.attack = abomination.attack - 2
            if boss_attack == "fast attack":
                P_S( combat_colour_font + "The abomination attack!" + reset_font_style)
                abomination.character_attack(player_character)
                player_alive_check(player_character)
                P_S( combat_colour_font + "You attack!" + reset_font_style)
                player_character.character_attack(abomination)
                final_boss_alive_check(abomination)
    P_S("" + reset_font_style)


def first_floor_action(player_character):
    """
    This fuctions will appear only in the first floor for the next floors
    the actions are different.

    Args:
        player_character (Class): This is the instance created in the main function.
        It is the player and will be persistent until the end of the game.
    """
    P_S(
        description_colour_font
        + "Dust covers everything in the halls, market stalls appear abandoned"
    )
    P_S("As if they all left in a rush")
    P_S("The halls might have something of value")
    P_S("" + reset_font_style)
    while True:
        P_S(floor_choice_colour + "What do you want to do?")
        first_floor_choice = input(
            """
        1- Search the stalls
        2- Continue your quest!
        """
            + reset_font_style
        )
        if first_floor_choice in ("1","2"):
            if first_floor_choice == "1":
                if chance_of_encounter(50) is True:
                    P_S(
                        description_colour_font
                        + "While searching for anything of value the sound"
                    )
                    P_S("a sudden cry pierces the silence and you turn just in time")
                    P_S("to see a strange creature charging!" + reset_font_style)
                    P_S(combat_colour_font + "Get ready!" + reset_font_style)
                    encounter(player_character)
                else:
                    P_S(
                        description_colour_font_2
                        + "You were ready to give up and complain about wasting time"
                    )
                    P_S("While a bright blade caught your eye a quick cleaning")
                    P_S("Reveals an extraordinary weapon that will surely help")
                    P_S("on what you will face ahead.")
                    P_S("You continue moving forward on your quest.")
                    P_S("" + reset_font_style)
                    player_character.attack = player_character.attack + 2
            elif first_floor_choice == "2":
                if chance_of_encounter(50) is True:
                    P_S(
                        description_colour_font_2
                        + "Moving forward you spot what looks like the stairs to"
                    )
                    P_S("The next level. You are almost at the start of the stairs")
                    P_S("When the clash and metal and stone draw your attention")
                    P_S("A lonely creature is approaching..." + reset_font_style)
                    P_S(combat_colour_font + "Get ready!" + reset_font_style)
                    encounter(player_character)
                else:
                    P_S(
                        description_colour_font_2
                        + "Moving forward you spot what looks like the stairs to"
                    )
                    P_S("The next level. You are almost at the start of the stairs")
                    P_S("Climbing the stairs is easy, the worn stone under your feet")
                    P_S(
                        "Is smooth. While walking you wondered what happened here.."
                        + reset_font_style
                    )
                    P_S("")
            break
        else:
            P_S(
                description_colour_font
                + "You need to select a valid option"
                + reset_font_style
            )
            continue

def second_floor_action(player_character):
    """
    Third floor action description. This present the player with a choice of continue exploring
    risking an encounter or keep moving forward.

    Args:
        player_character (Class): This is the instance created in the main function.
        It is the player and will be persistent until the end of the game.
    """
    P_S(
        description_colour_font_2
        + "Wandering through the dead city you spot the familiar sign of a smith"
    )
    P_S("It is a massive building the big forges are now dark and dead but")
    P_S("you can easily imagine how busy this building and the sound of hammering")
    P_S("There might be some items left behind inside the massive building")
    P_S("it will make you take a detour and add a few hours...would it be worthy it?")
    P_S("" + reset_font_style)
    while True:
        P_S(floor_choice_colour + "What do you want to do?")
        second_floor_choice = input(
            """
        1- Enter the forge
        2- Whatever is there is not worthy
        """
            + reset_font_style
        )
        if second_floor_choice in ("1","2"):
            if second_floor_choice == "1":
                if chance_of_encounter(50) is True:
                    P_S(
                        description_colour_font_2 + "The makeshift torch holds the darkness at bay"
                    )
                    P_S("hammers and anvils are starting to rust, some still have the pieces")
                    P_S("of steel over there as if waiting to be completed...")
                    P_S("Suddenly your hair stands up on the back of your neck a pair")
                    P_S("of eyes glow in the darkness getting closer..." + reset_font_style)
                    P_S(combat_colour_font + "Get Ready!" + reset_font_style)
                    encounter(player_character)
                else:
                    P_S(
                        description_colour_font_2 + "The makeshift torch holds the darkness at bay"
                    )
                    P_S("hammers and anvils are starting to rust, some still have the pieces")
                    P_S("of steel over there as if waiting to be completed...")
                    P_S("Suddenly your hair stands up on the back of your neck a pair")
                    P_S("You turn with your weapon ready....")
                    P_S("a quiet laugh escapes your lips. What looked like enemies is a row")
                    P_S("of armor stands..getting closer this marvelous craft still is usable")
                    P_S(
                        "You spot a shield the surface smooth and dusty but the straps are sturdy"
                    )
                    P_S("and the metal strong. You take it with you, any help is welcome here")
                    P_S("" + reset_font_style)
                    player_character.armour = player_character.armour + 2
            elif second_floor_choice == "2":
                P_S(
                    description_colour_font_2
                    + "You left the building behind an continue to move towards the main street"
                )
                P_S(
                "a wide avenue that in better time for sure would have been a breath taking sight"
                )
                P_S(
                    "the street appears to converge in what looks like the access to upwards..."
                )
                P_S("" + reset_font_style)
            break
        else:
            P_S(
                description_colour_font
                + "You need to select a valid option"
                + reset_font_style
            )
            continue

def third_floor_action(player_character):
    """
    Third floor action description. This present the player with a choice of continue exploring
    risking an encounter or keep moving forward.

    Args:
        player_character (Class): This is the instance created in the main function.
        It is the player and will be persistent until the end of the game.
    """
    P_S(
        description_colour_font_2
        + "The glittering of jewels makes you stop on your heels, the riches here"
    )
    P_S(
        "will be enough to live a life of comfort, but that is not what you are here for!"
        + reset_font_style
    )
    while True:
        P_S(floor_choice_colour + "What do you want to do?")
        P_S(
            """
            1- Enter and search
            2- That is not what I am here for!
            """
            + reset_font_style
        )
        third_floor_choice = input("")
        if third_floor_choice in ("1","2"):
            if third_floor_choice == "1":
                if chance_of_encounter(50) is True:
                    P_S(
                        description_colour_font_2
                        + "Your eyes can't believe the amount of diamonds, ruby and other"
                    )
                    P_S("many precious stones in the same room. You are roaming day dreaming")
                    P_S("about packing your bags with as many jewels and have a good life")
                    P_S("your hand is almost reaching to an exquisite crown when")
                    P_S("a gurgling noise rises from the end of the shop followed by a")
                    P_S("create stumbling towards you")
                    P_S("" + reset_font_style)
                    P_S(combat_colour_font + "Get ready!" + reset_font_style)
                    encounter(player_character)
                else:
                    P_S(
                        description_colour_font_2
                        + "Your eyes can't believe the amount of diamonds, ruby and other"
                    )
                    P_S("many precious stones in the same room. You are roaming day dreaming")
                    P_S("about packing your bags with as many jewels and have a good life.")
                    P_S(
                    "Wandering the room you endup in front of a display with a ring in the center"
                    )
                    P_S("you can swear that the ring glows but it is hard to tell. You reach for")
                    P_S("the ring. It feels warm and comforting in your hand. Suddenly the")
                    P_S("the old and new injuries seem to hurt less..")
                    P_S("" + reset_font_style)
                    player_character.health_points = player_character.health_points + 1
            else:
                P_S(
                    description_colour_font_2
                    + "You are no here for this! The final prize will all of this like a cheap"
                )
                P_S("glass and tin copy. Steeling yourself you push forward to the stair")
                P_S("leaving behind richness beyong your wildest dreams")
                P_S("" + reset_font_style)
            break
        else:
            P_S(
                    description_colour_font
                    + "You need to select a valid option"
                    + reset_font_style
                )
            continue

def main():

    """
    Main Game function
    """
    player_character = Player()
    player_character.max_health_points = 3
    player_character.health_points = 3

    print(
        title_colour_font
        + """
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
    """
        + reset_font_style
    )

    while True:
        player_character.name = input(
            description_colour_font
            + "Welcome to the tower what is your name adveturer?"
        )
        if player_character.name.isalpha():
            print(f"Very well {player_character.name} you are free to enter")
            break
        else:
            print(
                "I am afraid I only understsand letters"
                + reset_font_style
            )

    intro()
    first_floor()
    first_floor_action(player_character)
    second_floor()
    second_floor_action(player_character)
    thrid_floor()
    third_floor_action(player_character)
    final_fight(player_character)
    play_again()

if __name__ == "__main__":
    main()
