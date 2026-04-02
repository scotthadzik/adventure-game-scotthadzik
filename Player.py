class Player():

    inventory = []
    

    # initializer constructor
    def __init__(self):
        self.name = ""
        self.health = 100

    def get_name(self):
        # Ask for the player's name
        self.name = input("What is your name, adventurer? ") # return string (int 1) string "1"
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You picked up {item}, it has been added to your inventory")

    def is_item_in_inventory(self, item):
        # item = lantern
        # look at the inventory and check for a lantern
        # list -- array -- loop through a list 
        if item in self.inventory:
            return True
        return False