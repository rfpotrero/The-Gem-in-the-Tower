import time

def P_S(text):
    """
    Print the one line of of text and wait a certain amount of time
    before printing the following one. This helps the player to
    follow the story.

    Credits to Deanna Carina https://github.com/DeannaCarina/StarTrekTimeLoop/blob/main/functions.py
    I have slightly change the function to hardcoding the time parameters.
    """
    print(text)
    time.sleep(1)

def intro():
    """
    Displays the game game intro
    """
    P_S("The rest of your crew are missing or dead.")
    P_S("The few that survived the strom most likely did not survived the jungle")
    P_S("The tower is the only human construction you can see since days")
    P_S("and the gem on the top, as in the legends, shines like a light house")
    P_S("guiding you towards the city.")
    P_S(".....")
    P_S("")

def first_floor():
    """
    This display the first floor description.
    """
    P_S("The gates of the city towering before you. The walls are empty")
    P_S("No sentinels, no people just the eerie silence around you.")
    P_S("Placing your shoulder again the gate, it opened with a rasping")
    P_S("screech of rusty hinges.")
    P_S("The opened gate gave directly into a long, broad hall which ran away")
    P_S("and away until its vista grew indistinct in the distance.")

def second_floor():
    """
    This display the second floor description.
    """
    P_S("Your eyes widenen after reaching the end of the stairs")
    P_S("Before you appear what is seems a completed city the roof missing in the distance")
    P_S("No chambers, no gates. These people built their entery city inside.")
    P_S("Talls building surrounding you and the same eerie feeling floats around you")
    P_S("Searching through some of the shops and houses you see similar scenes")
    P_S("interrupted meals, works half finished but no bodies to be seen...")
    

def thrid_floor():
    """
    This display the third floor description.
    """
    P_S("The climbs ends up in a patio that even if it has seen better day")
    P_S("still you can tell it was constructed with the most expensive materials")
    P_S("rich marmol and jade mosaics cover the walls.")
    P_S("This probably is were the rulers and rich used to live")
    P_S("Massive villas like can be seen in the distance and a what probably")
    P_S("Is the access to top of the tower. A massive stairs of white stone")
    P_S("reflecting the light that enter through huge windows")
    P_S("you start to make your way to the stair.")
    P_S("Passing in front of what looks like luxurious shops you wonder")
    P_S("if there will be something of value left...")