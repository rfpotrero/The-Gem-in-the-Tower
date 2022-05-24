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
    P_S("Cutting through the thick wall of green is hard and takes time")
    P_S("by the time you leave the behid the jungle your arms feel like")
    P_S("if you have spend the entire day in battle.")
    P_S("The fatigue fell like chains of iron over your limbs and so you")
    P_S("decideto rest before the night close in")
    P_S("")

def first_floor():
    """
    This display the first floor description.
    """
    P_S("You arrived at the gates of the city before mid day. The walls are")
    P_S("empty. No sentinels, no people just the eerie silence around you.")
    P_S("Placing your shoulder again the gate, it opened with a rasping")
    P_S("screech of rusty hinges.")
    P_S("The opened gate gave directly into a long, broad hall which ran away")
    P_S("and away until its vista grew indistinct in the distance.")

def second_floor():
    """
    This display the second floor description.
    """
    pass

def thrid_floor():
    """
    This display the third floor description.
    """
    pass