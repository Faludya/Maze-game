
class Items:
    
    def __init__(self):
        self.coins = 0
        self.boomstick = 0
        self.pheonixBlaster = 0
        self.laser = 0
        self.teleporter1 = [12,23]
        self.teleporter2 = [20,2]
      

    #auxiliary function used when uploading a saved file
    def setItems(self, items):
        self.boomstick = items[0]
        self.pheonixBlaster = items[1]
        self.laser = items[2]
        self.coins = items[3]
 
    #auxiliary function used to see all weapons in the player's posession
    def allWeapons(self):
        weapons = []
        if self.boomstick != 0:
            weapons.append("boomstick")
        if self.pheonixBlaster != 0:
            weapons.append("pheonixBlaster")
        if self.laser != 0:
            weapons.append("laser")

        return weapons

    #auxiliary function used in "fight" to see if the player has any weapons
    def hasWeapon(self):
        if self.boomstick != 0:
            return "boomstick"
        if self.laser != 0:
            return "laser"
        if self.pheonixBlaster != 0:
            return "pheonixBlaster"
        return "none"
    
    #after each fight one weapon will be reset accordint to a specific order
    #(if the player has multiple weapons)
    def resetWeapons(self):
        if self.boomstick == 1:
            self.boomstick -= 1
            return
        if self.pheonixBlaster == 1:
            self.pheonixBlaster -= 1
            return
        if self.laser == 1:
            self.laser -= 1
            return
      
    #because we are clearing the maze at the position anyway in the move() function
    #here we only need to check if at the new position we have items to pick up
    def checkItems(self, coordinates, labyrinth):
        if labyrinth[coordinates[0]][coordinates[1]] == "*":
            self.coins += 100
        elif labyrinth[coordinates[0]][coordinates[1]] == "!":
            self.laser += 1
        elif labyrinth[coordinates[0]][coordinates[1]] == "(":
            self.boomstick += 1
        elif labyrinth[coordinates[0]][coordinates[1]] == ":":
            self.pheonixBlaster += 1  
        elif labyrinth[coordinates[0]][coordinates[1]] == "O":
            self.teleport(coordinates, labyrinth)
            
          
    #after teleporting, our location will be next to the teleporter       
    def teleport(self, coordinates, labyrinth):
        if coordinates == self.teleporter1:
            coordinates[0] = self.teleporter2[0] - 1
            coordinates[1] = self.teleporter2[1]
        else:
            coordinates[0] = self.teleporter1[0] 
            coordinates[1] = self.teleporter1[1] - 1
    
    

                
