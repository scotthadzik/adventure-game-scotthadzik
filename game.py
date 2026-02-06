"""
Adventure Game
Author: Scott Hadzik
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

inventory = []

def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")

    # Ask for the player's name
    player_name = input("What is your name, adventurer? ")
    
    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player_name}! Your journey begins now.")
    
    return player_name

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

player_name = welcome_player()
describe_area()

# Ask the player for their first decision
decision = input("What will you do (1, 2, 3, or i): ").lower()

# Respond based on the player's decision
if decision == "1":
    print(f"{player_name}! , you step into the dark woods...")
    add_to_inventory("lantern")
elif decision == "2":
    print(f"{player_name}! , you step into the mountain pass...")
    add_to_inventory("map")
elif decision == "3":
    print(f"{player_name}! , you don't go anywhere...")
elif decision == "i":
    print(f"{player_name}! this is your inventory")
else:
    print("Confused, you stand still, unsure of what to do.")