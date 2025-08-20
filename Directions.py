from Items import Items


class Directions:
    
    def __init__(self):
        #contain the [x,y] coordinates
        self.location = [1,1]
        self.winLocation = [23,24]
        self.Itm = Items()
   
    #auxiliary function to set the values to those of the saved game
    def uploadSave(self,prevLoc, savedItm):
        self.location[0] = prevLoc[0]
        self.location[1] = prevLoc[1]
        self.Itm.setItems(savedItm)

    #funtion used to move down in the maze
    def moveDown(self, labyrinth):
        #if there is a wall in the direction we want to move
        if labyrinth[self.location[0]+1][self.location[1]] == "X":
            print("Obstruction in the way!")
        else:
            #if there is nothing blocking the way
            #replace player location with blank space
            labyrinth[self.location[0]][self.location[1]] = " "
            #increase the "x" coordinate
            self.location[0] += 1
            #before replacing the new location, we check to see if we can pick up any items
            self.Itm.checkItems(self.location, labyrinth)
            #replace the new location with P to update the maze
            labyrinth[self.location[0]][self.location[1]] = "P"                   
            print("Path was clear!")

        
    def moveUp(self, labyrinth):
        #if there is a wall in the direction we want to move
        if labyrinth[self.location[0]-1][self.location[1]] == "X":
            print("Obstruction in the way!")
        else:
            #if there is nothing blocking the way
            #replace player location with blank space
            labyrinth[self.location[0]][self.location[1]] = " "
            #decrease the "x" coordinate
            self.location[0] -= 1
            #before replacing the new location, we check to see if we can pick up any items
            self.Itm.checkItems(self.location, labyrinth)
            #replace the new location with P to update the maze
            labyrinth[self.location[0]][self.location[1]] = "P"   
            print("Path was clear!")


    def moveRight(self, labyrinth):
        #if there is a wall in the direction we want to move
        if labyrinth[self.location[0]][self.location[1]+1] == "X":
            print("Obstruction in the way!")
        else:
            #if there is nothing blocking the way
            #replace player location with blank space
            labyrinth[self.location[0]][self.location[1]] = " "
            #increase the "y" coordinate
            self.location[1] += 1
            #before replacing the new location, we check to see if we can pick up any items
            self.Itm.checkItems(self.location, labyrinth)
            #replace the new location with P to update the maze
            labyrinth[self.location[0]][self.location[1]] = "P"   
            print("Path was clear!")
            
    def moveLeft(self, labyrinth):
        #if there is a wall in the direction we want to move
        if labyrinth[self.location[0]][self.location[1]-1] == "X":
            print("Obstruction in the way!")
        else:
            #if there is nothing blocking the way
            #replace player location with blank space
            labyrinth[self.location[0]][self.location[1]] = " "
            #decrease the "y" coordinate
            self.location[1] -= 1
            #before replacing the new location, we check to see if we can pick up any items
            self.Itm.checkItems(self.location, labyrinth)
            #replace the new location with P to update the maze
            labyrinth[self.location[0]][self.location[1]] = "P" 
            print("Path was clear!")
  
    #this function decides into which direction the player will move
    def move(self, new_direction,labyrinth):
        moves = "nsew"
        #check to see if the given direction is among the commands
        result = moves.find(new_direction)
        if result == -1:
            print("Invalid direction!")
            return
       
        if new_direction == "n":
            self.moveUp(labyrinth)
        elif new_direction == "s":
            self.moveDown(labyrinth)
        elif new_direction == "w":
           self.moveRight(labyrinth)
        elif new_direction == "e":
            self.moveLeft(labyrinth)
         
            

 
               
    
