
class Player:
    
    def __init__(self):
        #if each of these becomes 0 the game stops
        self.health = 201
        self.gameRunning = 1

    #setter used when uploading a saved file
    def setHealth(self, health):
        self.health = health
      
    #checks the conditions for loosing a game:
    def gameLost(self, playerCoord, enemyCoord, weapon, labyrinth):
        #enemy is on the same position
        if playerCoord[0] == enemyCoord[0] and playerCoord[1] == enemyCoord[1]:
            self.gameRunning = 0
        #after each fight, the player looses 100 health, and if it drops below 0 the player dies
        elif int(self.health) <= 0:
            self.gameRunning = 0
        #if it has no weapon and the enemy is in an adjacent position
        elif weapon == "none":   
           if ( (enemyCoord[0]+1 == playerCoord[0] and enemyCoord[1] == playerCoord[1]) or 
                (enemyCoord[0]-1 == playerCoord[0] and enemyCoord[1] == playerCoord[1]) or 
                (enemyCoord[1]+1 == playerCoord[1] and enemyCoord[0] == playerCoord[0]) or
                (enemyCoord[1]-1 == playerCoord[1] and enemyCoord[0] == playerCoord[0]) ):
               self.gameRunning = 0
        
    #check the conditions for a fight then performs it   
    def fight(self, Enemy, Directions, labyrinth):
        #1. if enemy is at an adjacent position
        if ( (Enemy.enemyPos[0]+1 == Directions.location[0] and Enemy.enemyPos[1] == Directions.location[1]) or 
             (Enemy.enemyPos[0]-1 == Directions.location[0] and Enemy.enemyPos[1] == Directions.location[1]) or 
             (Enemy.enemyPos[1]+1 == Directions.location[1] and Enemy.enemyPos[0] == Directions.location[0]) or 
             (Enemy.enemyPos[1]-1 == Directions.location[1] and Enemy.enemyPos[0] == Directions.location[0]) ) :
            #2. if we have at least one weapon
             if Directions.Itm.hasWeapon() != "none":
                #a) after a fight, the enemy is sent to his starting position
                Enemy.resetPosition(labyrinth)
                #b) the player consumes the weapon
                Directions.Itm.resetWeapons()
                #c) the player looses 100 health
                self.health -= 100
             else:
                 #if we cannot fight the enemy, it means it caught us
                self.gameRunning = 0
     
                
    #auxiliary function to print the status after each move      
    def printStatus(self, Directions):
        print("Location:", Directions.location)
        print("Score: ", Directions.Itm.coins)
        guns = Directions.Itm.allWeapons()
        print("Weapon: ", guns)
        
    