"""
This module contais the floor descriptions
and the function to display 1 line at a time.
"""

import time
from colored import fg, attr

title_colour_font = fg(69)
description_colour_font = fg(191)
description_colour_font_2 = fg(193)
floor_choice_colour = fg(214)
combat_colour_font = fg(125)
reset_font_style = attr(0)


def P_S(text):
    """
    Print the one line of of text and wait a certain amount of time
    before printing the following one. This helps the player to
    follow the story.

    Credits to Deanna Carina https://github.com/DeannaCarina/StarTrekTimeLoop/blob/main/functions.py
    I have slightly change the function to hardcoding the time parameters.
    Args:
        text (string): This is the string that will be displaying line by line.
    """
    print(text)
    time.sleep(0.7)


def intro():
    """
    Displays the game game intro
    """
    P_S("")
    P_S(description_colour_font + "The rest of your crew are missing or dead.")
    P_S("The few that survived the strom most likely did not survived the jungle")
    P_S("The tower is the only human construction you can see since days")
    P_S("and the gem on the top, as in the legends, shines like a light house")
    P_S("guiding you towards the city.")
    P_S("" + reset_font_style)


def first_floor():
    """
    This displays the first floor description.
    """

    P_S(
        description_colour_font_2
        + "The gates of the city towering before you. The walls are empty"
    )
    P_S("No sentinels, no people just the eerie silence around you.")
    P_S("Placing your shoulder against the gate, it opened with a rasping")
    P_S("screech of rusty hinges.")
    P_S("The opened gate gave directly into a long, broad hall which ran away")
    P_S("and away until its vista grew indistinct in the distance.")
    P_S("" + reset_font_style)


def second_floor():
    """
    This displays the second floor description.
    """
    P_S(
        description_colour_font
        + "Your eyes widened after reaching the end of the stairs"
    )
    P_S("Before you appear what seems a completed city encased within the walls")
    P_S("No chambers, no gates. These people built their entire city inside.")
    P_S("Tall buildings surrounding and the same eerie feeling floats around you")
    P_S("Searching through some of the shops and houses you see similar scenes")
    P_S("interrupted meals, works half finished but no bodies to be seen...")
    P_S("" + reset_font_style)


def thrid_floor():
    """
    This displays the third floor description.
    """
    P_S("")
    P_S(
        description_colour_font
        + "The stair ends up in a patio that even if it has seen better day"
    )
    P_S("still you can tell it was constructed with the most expensive materials")
    P_S("rich marmol and jade mosaics cover the walls.")
    P_S("This is where the rulers and rich used to live")
    P_S("Massive villas can be seen in the distance and what is probably")
    P_S("the access to the top of the tower. A massive stair of white stone")
    P_S("reflecting the light that enters through huge windows")
    P_S("you start to make your way to the stair.")
    P_S("Passing in front of what looks like luxurious shops you wonder")
    P_S("if there will be something of value left...")
    P_S("" + reset_font_style)

def final_fight_description():
    """
    This function describes the final fight.
    """
    P_S(
        description_colour_font
        + "You climb the last flight and reach the old throne room"
    )
    P_S("The rotten meat smell is everywhere, with horror you understand")
    P_S("Now where the bodies of the inhabitants are...")
    P_S("Human skink decorates the walls as terribles tapestries and in the middle")
    P_S("A column of twisted flesh rises with the gem on top")
    P_S("You can make the faces and limbs in that horrendous construction")
    P_S("")
    P_S("Before you, the guardian of this terrible room starts to rise. An abomination")
    P_S("The monstrous creature wears human remains as an improvised armor")
    P_S("Moving towards you a blade of bone appears from what looks like their arm")
    P_S("Steeling yourself, you firmly grip your own sword and face the creature")
    P_S("" + reset_font_style)


def player_final_fight_victory():
    """
    This function will display the description of the player winning
    """
    P_S(
        description_colour_font
        + "The abomination lays dead at your feet completely inmobile. "
    )
    P_S("The changing faces and twisted limb that just a moment")
    P_S("wanted to tear you apart are finally resting. You shudder at the destiny of")
    P_S("the dwellers of the city. Such a horrible fate.")
    P_S(
        "Turning to the last steps you can see the gem finally at reach!"
        + reset_font_style
    )
    P_S("")
    game_ending_description()

def game_ending_description():
    """
    Game ending description
    """
    P_S(
        description_colour_font_2
        + "The gem shines in front of you. The legends were right!")
    P_S("The facets reflect the light in impossible shapes")
    P_S("With this you could buy entire kingdoms. The gem is light and strangely")
    P_S("warm in your palm. Putting inside your velvet pouch you are ready to leave")
    P_S("this horrible place.")
    P_S("Nothing bothers you on the way down, all seem strangely calm but you")
    P_S("breath once outside the walls and under the open skies")
    P_S("The walk to your ship will be a long one but you are optimistic")
    P_S("" + reset_font_style)

def player_death():
    """
    This functions gives a brief description when the player health_point reach zero
    """
    P_S(description_colour_font +
        "The last thing you see is a blow passing your defense. You almost felt no pain"
    )
    P_S("with darkness engulfing you. The monster stands before you baring their fangs")
    P_S("....." + reset_font_style)
