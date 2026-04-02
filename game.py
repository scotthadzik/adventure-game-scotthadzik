from Player import Player

"""
Adventure Game
Author: Scott Hadzik
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

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
        4. Stay where you are.
        Type 'i' to view your inventory.
        Type 'q' to quit
    """
    print(starting_area)



welcome_player() # Scott

player = Player() # instance of the Player Class -- Object
player.get_name()

# Use an f-string to display the same message in a more readable way
print(f"Welcome, {player.name}! Your journey begins now.")

describe_area()
while True:
    # Ask the player for their first decision
    decision = input("What will you do (1, 2, 3, 4, i, q (quit)):").lower()

    # while loop -> when we don't know the of times to loop
    # for loop -> when we know the number of times to loop
    # do while -> Execute at least once. condition is at the bottom

    # Respond based on the player's decision
    if decision == "1":
        print(f"{player.name}, you step into the dark woods...")
        player.add_to_inventory("lantern")
    elif decision == "2":
        print(f"{player.name}, you step onto the path into the mountains...")
        player.add_to_inventory("map")
    elif decision == "3": # cave
        # if the player has the lantern they can enter the cave
        if player.is_item_in_inventory("lantern"):
            print(f"{player.name}, you enter the cave")
        else:
            print("It is too dark to go into the cave")
    elif decision == "4":
        print(f"{player.name}, you stay where you are")
    elif decision == "i":
        print(player.inventory)
    elif decision == "q":
        print("Thanks for playing")
        break
    else:
        print("Confused, you stand still, unsure of what to do.")



