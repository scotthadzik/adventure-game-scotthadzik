"""
Adventure Game
Author: Scott Hadzik
Version: 3.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest. Now uses inventory and flags to affect gameplay.
"""

# -----------------------------
# Player class to store player info and game state
# -----------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

# -----------------------------
# Welcome the player and create the Player object
# -----------------------------
def welcome_player():
    name = input("What is your name, adventurer? ")
    player = Player(name)
    print(f"Welcome, {player.name}! Your journey begins now.")
    return player

# -----------------------------
# Describe the starting area
# -----------------------------
def describe_area():
    print("""
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the unknown...
    """)

# -----------------------------
# Add item to the player's inventory
# -----------------------------
def add_to_inventory(player, item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")

# -----------------------------
# explore_dark_woods
# describes dar woods
# add the lantern to inventory
# -----------------------------
def explore_dark_woods(player):
    print(f"{player.name}, you step into the dark woods...")
    
    # if they do not have the lantern
    if "lantern" not in player.inventory:
        add_to_inventory(player, "lantern")
        player.has_lantern = True
    else:
     print("You've already found the lantern here!")

# -----------------------------
# Mountain pass area
# -----------------------------
def explore_mountain_pass(player):
    print(f"{player.name}, you head toward the mountain pass...")
    if "map" not in player.inventory:
        add_to_inventory(player, "map")
        player.has_map = True
    else:
        print("You've already picked up the map from here!")

# -----------------------------
# Cave area
# -----------------------------
def explore_cave(player):
    # Conditional logic: need lantern to explore the cave
    if player.has_lantern:
        print(f"{player.name}, you bravely enter the dark cave, your lantern lighting the way.")
        if "treasure" not in player.inventory:
            print("Inside the cave, you find hidden treasure!")
            add_to_inventory(player, "treasure")
        else:
            print("You already collected the treasure for the cave")
    else:
        print("It’s too dark to explore the cave without a lantern!")
        print("Maybe you should find a light source first.")

# TODO: Create a function called explore_hidden_valley(player)
#       - If player.has_map: allow entry and add "rare herbs"
#       - Else: warn that player can't find the valley
def explore_hidden_valley(player):
    # Conditional logic: need map to find the hidden valley
    if player.has_map:
        print(f"{player.name}, you study the map carefully...")
        if "rare herbs" not in player.inventory:
            print("You discover a hidden path to a beautiful secret valley filled with rare herbs!")
            add_to_inventory(player, "rare herbs")
        else:
            print("You already have the rare herbs")
    else:
        print("You wander in circles, unable to find anything special without a map.")

# -----------------------------
# Main program
# -----------------------------
player = welcome_player()
describe_area()

while True:
    print("\nYou see several choices ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Explore a nearby cave.")
    print("\t4. Search for a hidden valley.")
    print("\t5. Stay where you are.")
    print("\tType 'i' to view your inventory.")

    decision = input("What will you do (1, 2, 3, 4, 5, or i): ").lower()

    if decision == "i":
        print("Inventory:", player.inventory)
        continue

    if decision == "1":
       explore_dark_woods(player)
    
    elif decision == "2":
        explore_mountain_pass(player)
    
    elif decision == "3":
        explore_cave(player)

    elif decision == "4":
        explore_hidden_valley(player)

    elif decision == "5":
        print("You stay still, listening to the sounds of the forest.")
    
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, 5, or 'i'.")

    # Ask if the player wants to continue
    play_again = input("Do you want to continue exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name}. See you next time!")
        break