"""
Adventure Game
Author: Scott Hadzik
Version: 2.2
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
        print(f"{player.name}, you step into the dark woods...")
        add_to_inventory(player, "lantern")
        player.has_lantern = True
    
    elif decision == "2":
        print(f"{player.name}, you head toward the mountain pass...")
        add_to_inventory(player, "map")
        player.has_map = True
    
    elif decision == "3":
        # Conditional logic: need lantern to explore the cave
        if player.has_lantern:
            print(f"{player.name}, you bravely enter the dark cave, your lantern lighting the way.")
            print("Inside the cave, you find hidden treasure!")
            add_to_inventory(player, "treasure")
        else:
            print("It’s too dark to explore the cave without a lantern!")
            print("Maybe you should find a light source first.")
    elif decision == "4":
        # Conditional logic: need map to find the hidden valley
        if player.has_map:
            print(f"{player.name}, you study the map carefully...")
            print("You discover a hidden path to a beautiful secret valley filled with rare herbs!")
            add_to_inventory(player, "rare herbs")
        else:
            print("You wander in circles, unable to find anything special without a map.")
    elif decision == "5":
        print("You stay still, listening to the sounds of the forest.")
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, 5, or 'i'.")

    # Ask if the player wants to continue
    play_again = input("Do you want to continue exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name}. See you next time!")
        break