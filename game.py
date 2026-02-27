"""
Adventure Game
Author: Scott Hadzik
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

from Player import Player

 # Object or instance of the Player class

# TODO: Replace the global variable player_name with a Player object
#       Example: player = Player("Scott")

# TODO: Update your welcome_player() function to return a Player object
#       Instead of returning just a name, create and return the Player

# TODO: Update add_to_inventory() so it:
#       - Accepts a Player object as a parameter
#       - Appends the item to player.inventory
#       - Prints a message confirming the item was picked up

# TODO: In path 1, after picking up the lantern:
#       - Set player.has_lantern = True

# TODO: In path 2, after picking up the map:
#       - Set player.has_map = True

# TODO: (Optional Stretch) Add a check before certain choices
#       - Example: If player.has_lantern is False, prevent entering a cave
#       - Print a message like “It’s too dark to continue without a lantern.”

# TODO: Update all print statements that used player_name to use player.name

# TODO: Commit and push your code with a message like:
#       REF player class added and game state flags implemented


inventory = [""]

def welcome_player():  # DRY Do not repeat yourself reusability debug
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")

    # Ask for the player's name
    player_name = input("What is your name, adventurer? ")
    player = Player(player_name) # Scott

    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player.name}! Your journey begins now.")
    
    return player

def describe_area():
    # Describe the starting area
    starting_area = """
    You find yourself in a dark forest...
        You see two paths ahead:
        1. Take the left path into the dark woods.
        2. Take the right path toward the mountain pass.
        3. Stay where you are.
        Type 'i' to view your inventory.
    """
    print(starting_area)

def add_to_inventory(item):
    inventory.append(item)
    print(f"{item} was added to your inventory")

player1 = welcome_player()
describe_area()

# Ask the player for their first decision
decision = input("What will you do (1, 2, 3, or i): ").lower() # returns a string

# Respond based on the player's decision
if decision == "1": # decision + 7 = invalid "1" equivalent to "1" = means assign
    print(f"{player1.name}! , you step into the dark woods...")
    add_to_inventory("lantern")
elif decision == "2":
    print(f"{player1.name}! , you step into the mountain pass...")
    add_to_inventory("map")
elif decision == "3":
    print(f"{player1.name}! , you don't go anywhere...")
elif decision == "i":
    print(f"{player1.name}! this is your inventory")
else:
    print("Confused, you stand still, unsure of what to do.")