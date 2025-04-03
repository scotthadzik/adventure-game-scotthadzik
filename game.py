'''
DOCSTRING
Adventure Game
Author: Scott Hadzik
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

TODOs

# TODO: Create a class called Player to represent the player in the game

# TODO: Inside the Player class, define an __init__ method that:
#       - Takes a name parameter
#       - Initializes these attributes:
#         - self.name (string)
#         - self.inventory (empty list)
#         - self.health (set to 100)
#         - self.has_map (set to False)
#         - self.has_lantern (set to False)

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


#----------------------
# Global inventory list
# This will hold items the player collects
#----------------------
inventory = []

#----------------
# Function: welcome_player
# Greets the player, asks for their name,
# and returns the name as a string
#----------------
def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print('Your journey begins here... ')

    # Ask for the player's name
    player_name = input("What is your name, adventurer? ")

    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player_name}! Your journey begins now.")

    return player_name

#----------------
# Function: describe_area
# Print the opening description of the area
#----------------
def describe_area():
    # Describe the starting area
    print( """
    You find yourself in a dark forest
    The sound of rustling leaves fills the air
    A faint path lies ahead, leading deeper into the
    unknown... """)

#----------------
# Function: add_to_inventory
# Accepts an item name as a parameter,
# adds it to the inventory list,
# and confirm the pickup to the player
#----------------
def add_to_inventory(item):
    inventory.append(item)
    print(f"You picked up a {item}!")

#-----------------
# Game starts here
# Call the welcome and describe area functions
#-----------------

player_name = welcome_player()
describe_area()

#-----------------
# Main game loop
# run this until the player quiescent
#-----------------

# Start the game Loop
while True:
    print("\nYou see two paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")
    print("\tType 'i' to view your inventory.")

    decision = input("What will you do (1,2,3 or i): ").lower()

    if decision == 'i':
        print("Inventory", inventory)
        continue

    if decision == "1":
        print(f"{player_name}, you step into the dark woods."
              "The trees whisper as walk deeper.")
        add_to_inventory("lantern")
    elif decision == "2":
        print(f"{player_name}, you make your way "
              "towards the mountain pass, feeling "
              "the cold wind against your face.")
        add_to_inventory("map")
        
    elif decision == "3":
        print("You stay still, listening to the " 
              "distant sounds of the forest")
    else: 
        print("Invalid choice. Please choose "
              "1, 2, or 3.")
    
    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player_name} "
              "See you next time.")
        break # Exit the loop and end the game
    
