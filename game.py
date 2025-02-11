'''
DOCSTRING
Adventure Game
Author: Scott Hadzik
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

# Welcome message and introduction
print("Welcome to the Adventure Game!")  
print('Your journey begins here... ')

# Ask for the player's name
player_name = input("What is your name, adventurer? ")

# Concatenate strings to create a personalized message
print("Welcome, " + player_name + "! Your journey begins now.")

# Use an f-string to display the same message in a more readable way
print(f"Welcome, {player_name}! Your journey begins now.")

# Describe the starting area
starting_area = """
You find yourself in a dark forest
The sound of rustling leaves fills the air
A faint path lies ahead, leading deeper into the
unknown... 
"""
print(starting_area)

# Start the game Loop
while True:
    print("\nYou see two paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")

    decision = input("What will you do (1,2,3): ")

    if decision == "1":
        print(f"{player_name}, you step into the dark woods."
              "The trees whisper as walk deeper.")
    elif decision == "2":
        print(f"{player_name}, you make your way "
              "towards the mountain pass, feeling "
              "the cold wind against your face.")
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
    