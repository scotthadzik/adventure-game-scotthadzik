from Player import Player

"""
Adventure Game
Author: Scott Hadzik
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""




# TODO: Create a function check_lose(player)
#       - If health is 0 or lower, print lose message and exit
# TODO: Show the player's current health after every action
# TODO: Continue using good Git habits: save, commit, push!
# TODO: Final commit message example: "COMPLETE Final Adventure Game"



def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...") 

def describe_area():
    # Describe the starting area
    starting_area = """
    You find yourself in a dark forest...
    You see three paths ahead:
        1. Take the left path into the dark woods.
        2. Take the right path toward the mountain pass.
        3. Take the center path towards the cave
        4. Take the path to the hidden valley
        5. Stay where you are.
        Type 'i' to view your inventory.
        Type 'q' to quit
    """
    print(starting_area)

def explore_the_dark_woods(player):
     print(f"{player.name}, you step into the dark woods...")
     player.add_to_inventory("lantern")

def explore_the_mountain_pass(player):
    print(f"{player.name}, you step onto the path into the mountains...")
    player.add_to_inventory("map")

def explore_the_cave(player):
    # if the player has the lantern they can enter the cave
    if player.is_item_in_inventory("lantern"):
        print(f"{player.name}, you enter the cave")
        player.add_to_inventory("treasure")
    else:
        print("It is too dark to go into the cave")
        player.health -= 10
        print(f"Your health is now {player.health}")

def explore_the_hidden_valley(player):
    # Go in the valley if map, treasure
    if player.is_item_in_inventory("map") and player.is_item_in_inventory("treasure"):
        print(f"{player.name}, you enter the hidden valley")
        player.add_to_inventory("rare herbs")
    else:
        print(f"{player.name}, you do not have the required items to enter the valley")
        player.health -= 10
        print(f"Your health is now {player.health}")

def stay_still(player):
    player.health -= 10  #  health = health - 10
    print(f"Your health is now {player.health}")

def check_win(player):
    if player.is_item_in_inventory("rare herbs"):
        print(f"{player.name} you have won the game")
        return True
    else:
        return False

def check_lose(player):
    if player.health <= 0:
        print(f"{player.name} you have died")
        return True
    else:
        return False

welcome_player() # Scott

player = Player() # instance of the Player Class -- Object
player.get_name()

# Use an f-string to display the same message in a more readable way
print(f"Welcome, {player.name}! Your journey begins now.")

describe_area()
while True:
    # Ask the player for their first decision
    decision = input("What will you do (1, 2, 3, 4, 5, i, q (quit)):").lower()

    # while loop -> when we don't know the of times to loop
    # for loop -> when we know the number of times to loop
    # do while -> Execute at least once. condition is at the bottom

    # Respond based on the player's decision
    if decision == "1": # dark woods
        explore_the_dark_woods(player)
    elif decision == "2": # mountain pass
        explore_the_mountain_pass(player)
    elif decision == "3": # cave
        explore_the_cave(player)
    elif decision == "4": # Hidden Valley
        explore_the_hidden_valley(player)
    elif decision == "5": # stay where you are
        print(f"{player.name}, you stay where you are")
        stay_still(player)
    elif decision == "i":
        print(player.inventory)
    elif decision == "q":
        print("Thanks for playing")
        break
    else:
        print("Confused, you stand still, unsure of what to do.")

    if check_win(player):
        break
    if check_lose(player):
        break


