# from gpiozero import LED
from time import sleep

# TODO: Set up the LEDs

# Start the infinite loop
while True:

    user_input = input("input 'red', 'green', or 'q' to quit ").lower()

    # TODO: Create the logic for when the input is 'red'
    # Turn on the red LED for 20 seconds and turn off the green LED
    if user_input == 'red':
        print( "turn on red turn off green")
        print("Red is ON")
        red.on()
        green.off()
        sleep(1)
        
    elif user_input == 'green':
        print( "turn off red turn on green")
    # Check if the input is 'q' (quit)
    elif user_input == 'q':
        print("Quitting the program.")
        # TODO: Turn off both LEDs before quitting the program
        break # Exit the loop and end the program
    else:
        # If the input is invalid, prompt the user to enter a valid choice
        print("Invalid input. Please enter 'red', 'green', or 'q'.")
    red.off()
    green.off()
    # TODO: After the 20-second delay, make sure both LEDs are turned off
    # This will prepare the LEDs for the next input