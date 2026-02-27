# Class is a blueprint of the object
class Player:
    
    # initializer constructor
    def __init__(self, name): # must use self some use this
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False