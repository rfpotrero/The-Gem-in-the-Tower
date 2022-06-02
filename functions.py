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
    P_S("Second floor descriotion!!")

def thrid_floor():
    """
    This display the third floor description.
    """
    P_S("Third floor description!")
