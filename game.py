"""
Adventure Game
Author: Scott Hadzik
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

from Player import Player

def welcome_player():  # DRY Do not repeat yourself reusability debug
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")

def describe_area():
    # Describe the starting area
    starting_area = """
    You find yourself in a dark forest...
        You see two paths ahead:
        1. Take the left path into the dark woods.
        2. Take the right path toward the mountain pass.
        3. Take the middle path to the cave
        4. Take the path to the hidden valley
        5. Stay where you are.
        Type 'i' to view your inventory.
        Type 'q' to quit
    """
    print(starting_area)

def explore_the_dark_woods(player):
    print(f"{player.name}! , you step into the dark woods...")
    player.add_to_inventory("lantern")

def explore_the_mountain_pass(player):
    print(f"{player.name}! , you step into the mountain pass...")
    player.add_to_inventory("map")

def explore_the_cave(player):
# only allow player in the cave if they have the lantern
    if player.is_item_in_inventory("lantern"):
        print(f"{player.name}, you enter the cave")
        player.add_to_inventory("treasure")
    else:
        print(f"{player.name}! , you must have a lantern to enter the cave")
        player.take_damage(10)

def explore_the_hidden_valley(player):
    if player.is_item_in_inventory("map"):
        print(f"{player.name}! , you enter the hidden valley")
        player.add_to_inventory("rare herbs")
    else:
        print("You can't find the valley")
        player.take_damage(10)

def stay_still(player):
    print(f"{player.name}! , you don't go anywhere...")
    # subtract 10 health from the player
    player.take_damage(10)

def check_win(player):
    # treasure rare herbs
    if player.is_item_in_inventory("treasure") and player.is_item_in_inventory("rare herbs"):
        print(f"{player.name}, you have won the game!")
        return True
    else:
        return False

def check_dead(player):
    if player.health <= 0:
        print(f"{player.name} has died!")
        return True
    else:
        return False

welcome_player()
player = Player() # Instance of the Player Class
player.ask_player_name()
# Use an f-string to display the same message in a more readable way
print(f"Welcome, {player.name}! Your journey begins now.")
describe_area()


# loop repeat code
# for loop --> when we know how many time the loop will execute
# while loop --> when we don't know how many times the loop will execute

while True: # condition like if (decision !=q) <--- unknown decision -- do/while
    # Ask the player for their first decision
    decision = input("What will you do (1, 2, 3, 4, 5, i, q (quit)): ").lower() # returns a string
    # Respond based on the player's decision
    match decision:
        case "1": # decision + 7 = invalid "1" equivalent to "1" = means assign
            explore_the_dark_woods(player)
        case "2":
            explore_the_mountain_pass(player)
        case "3":
            explore_the_cave(player)
        case "4":
            explore_the_hidden_valley(player)
        case "5":
            stay_still(player)
        case "i":
            print(f"{player.name}! this is your inventory")
            print(player.inventory)
        case "q":
            print(f"{player.name}! Thanks for playing")
            break
        case _:
            print("Confused, you stand still, unsure of what to do.")
        
    print ("")
    if check_win(player) or check_dead(player): # if true
        break