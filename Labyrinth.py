from Enemy import Enemy

class Labyrinth:
    
    def __init__(self):
        self.labyrinth = []
        
    #loads the start game
    def loadStartFile(self):
         inputFile = open("maze.txt", "r")
         content = inputFile.readlines()
         self.labyrinth = [[character for character in line] for line in [word.strip('\n') for word in content]]
         inputFile.close()

    #loads a previously saved game
    def loadSavedFile(self, Directions, Player, enemyList, Labyrinth):
        inputFile = open("save.txt", "r")
        content = inputFile.readlines()
        #first line contains the coordinates for the player's last location
        x, y = int(content[0].split()[0]), int(content[0].split()[1])
        savedLoc = [x,y]     
        #second line says if it had the weapon boomstick: 0 for false, 1 for true
        boomstick = int(content[1][0]) 
        #same for the next two weapons, pheonixBlaster and laser
        pheonixBlaster = int(content[2][0])
        laser = int(content[3][0])     
        #total number of coins that the player picked up
        coins = int(content[4])        
        #all these items are united in a list and given as parameter to be uploaded in Directions
        items = [boomstick, pheonixBlaster, laser, coins] 
        Directions.uploadSave(savedLoc, items) 
        #on the sixth line is the health the player had in the game
        health = int(content[5]) 
        Player.setHealth(health)
     
        #on each of the followint four line it is given the last location of each enemy
        #when we create a new entity we have to keep in mind the location that the monster will be 
        #reset to when hit by a weapon. This location is picked individually for each monster
        enemyList.append(Enemy([int(content[6].split()[0]), int(content[6].split()[1])], [6,18]))
        enemyList.append(Enemy([int(content[7].split()[0]), int(content[7].split()[1])], [14,3]))
        enemyList.append(Enemy([int(content[8].split()[0]), int(content[8].split()[1])], [19,23]))
        enemyList.append(Enemy([int(content[9].split()[0]), int(content[9].split()[1])], [23,4]))

        #the rest of the text file will be the maze itself.
        tempLab = content[10:]
        Labyrinth.labyrinth = [[character for character in line] for line in [word.strip('\n') for word in tempLab]]

     
    #write in a text file the details needed to start a game from this state
    def uploadFile(self, Directions, Player, enemyList, Labyrinth):
        inputFile = open("save.txt", "w")
        #convert the location of the player into a string of type: 4 13
        line = str(Directions.location[0]) + " " + str(Directions.location[1])
        inputFile.write(line) #player position
        inputFile.write("\n")
        #if player had boomstick weapon: 0 for false, 1 for true
        inputFile.write(str(Directions.Itm.boomstick))
        inputFile.write("\n")
        #if player had pheonixBlaster weapon: 0 for false, 1 for true
        inputFile.write(str(Directions.Itm.pheonixBlaster))
        inputFile.write("\n")
        #if player had laser weapon: 0 for false, 1 for true
        inputFile.write(str(Directions.Itm.laser))
        inputFile.write("\n")
        #total number of coins the player currently has
        inputFile.write(str(Directions.Itm.coins))
        inputFile.write("\n")
        #total health player has at this point
        inputFile.write(str(Player.health))
        inputFile.write("\n")
        #convert the positions of enemies into a string of type: 15 2
        for x in range (4):
            line = str(enemyList[x].enemyPos[0]) + " " + str(enemyList[x].enemyPos[1])
            inputFile.write(line)
            inputFile.write("\n")
        #at last, write the maze as it is currently
        inputFile.write('\n'.join([''.join([str(cell) for cell in row]) for row in self.labyrinth]))

    #prints labyrinth into a nicer format
    def printLabyrinth(self):
       print('\n'.join([''.join([str(cell) for cell in row]) for row in self.labyrinth]))


    def printIntroduction(self):
        print("************Welcome to the Maze Game************")
        print("To start a new game write start")
        print("To load a previously saved game write load")
        print("To exit the game write quit")
        print("************Enjoy the maze************\n\n")


    
