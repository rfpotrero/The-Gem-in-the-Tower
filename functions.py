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
    P_S("The rest of your crew is missing or dead")
    P_S("The few that survived the strom most likely")
    P_S("did not make it through the jungle but that is the")
    P_S("price of civilisation, dull senses and weak bodies")
    P_S("Now you stand in the front of the tower")


def first_floor():
    """
    This display the first floor description.
    """
    P_S("Without any delay you start to make your way up")
    P_S("The air smell damp and there is the lingering sweet")
    P_S("Aroma of rotting vegetation")
    

def second_floor():
    pass

def thrid_floor():
    pass
    