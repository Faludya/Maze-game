import random

class Enemy:
    def __init__(self, current, start):
        self.enemyPos = current
        self.startPos = start
      
    #after we fight an enemy, it will be reset to its starting position  
    def resetPosition(self, labyrinth):
        labyrinth[self.enemyPos[0]][self.enemyPos[1]] = " "
        self.enemyPos = self.startPos
        labyrinth[self.enemyPos[0]][self.enemyPos[1]] = "E"
        
    #in order to give them a much more "random" appearance, if the random position decides to move them
    #towards a wall, the function will be called again so as not to have them blocked into a space   
    def enemyMoveUp(self, labyrinth):
        #enemies can't move on teleporters
        if (labyrinth[self.enemyPos[0]-1][self.enemyPos[1]] == "X" or
            labyrinth[self.enemyPos[0]-1][self.enemyPos[1]] == "O"):
            self.enemyMove(labyrinth)
        else:
            labyrinth[self.enemyPos[0]][self.enemyPos[1]] = " "
            self.enemyPos[0] -= 1
            labyrinth[self.enemyPos[0]][self.enemyPos[1]] = "E"
    
    
    def enemyMoveDown(self, labyrinth):
        if (labyrinth[self.enemyPos[0]+1][self.enemyPos[1]] == "X" or
            labyrinth[self.enemyPos[0]+1][self.enemyPos[1]] == "O"):
            self.enemyMove(labyrinth)
        else:
            labyrinth[self.enemyPos[0]][self.enemyPos[1]] = " "
            self.enemyPos[0] += 1
            labyrinth[self.enemyPos[0]][self.enemyPos[1]] = "E"
    
    def enemyMoveRight(self, labyrinth):
        if (labyrinth[self.enemyPos[0]][self.enemyPos[1]+1] == "X" or
            labyrinth[self.enemyPos[0]][self.enemyPos[1]+1] == "O"):
            self.enemyMove(labyrinth)
        else:
            labyrinth[self.enemyPos[0]][self.enemyPos[1]] = " "
            self.enemyPos[1] += 1
            labyrinth[self.enemyPos[0]][self.enemyPos[1]] = "E"
    
    def enemyMoveLeft(self, labyrinth):
        if (labyrinth[self.enemyPos[0]][self.enemyPos[1]-1] == "X" or
            labyrinth[self.enemyPos[0]][self.enemyPos[1]-1] == "O"):
            self.enemyMove(labyrinth)
        elif labyrinth[self.enemyPos[0]][self.enemyPos[1]-1] == " ":
            labyrinth[self.enemyPos[0]][self.enemyPos[1]] = " "
            self.enemyPos[1] -= 1
            labyrinth[self.enemyPos[0]][self.enemyPos[1]] = "E"
    
    #the movement is decided randomly. As said before, whenever the enemy will encounter a wall it will 
    #call this fucntion again to decide a new direction of movement
    def enemyMove(self, labyrinth):
        randDir = random.randint(1, 4)
        if randDir == 1:
            self.enemyMoveUp(labyrinth)
        elif randDir == 2:
            self.enemyMoveDown(labyrinth)
        elif randDir == 3:
            self.enemyMoveRight(labyrinth)
        else:
            self.enemyMoveLeft(labyrinth)
         
    #auxiliary function used at the end of a game to print the location of each enemy
    def printEnemyStatus(self):
        print("Enemy location: ", self.enemyPos)