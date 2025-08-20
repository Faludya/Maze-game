from Labyrinth import Labyrinth
from Directions import Directions
from Player import Player
from Enemy import Enemy
import os

def main():
    #initializations
    Lab = Labyrinth()
    Dir = Directions()
    Plr = Player()
    enemyList = []

    #at the begining we have 3 options: start, load, quit
    Lab.printIntroduction()  
    x = input("Enter your option: ")
    if x == "start":
        Lab.loadStartFile()
        enemyList = [Enemy([6,18], [6,18]), 
                     Enemy([14,3], [14,3]), 
                     Enemy([19,23], [19,23]), 
                     Enemy([23,4], [23,4]) ]
    elif x == "load":
        Lab.loadSavedFile(Dir, Plr, enemyList, Lab)
    elif x == "quit":
        return
    else:
        print("Invalid command")
    #clear the console, works in vs by pressing crtl+f5. It gives the game a fluid appearance
    os.system('cls')

    Plr.printStatus(Dir)
    Lab.printLabyrinth()

    #while game is running
    while Dir.location != Dir.winLocation and Plr.gameRunning == 1:
        #before moving we need to check if an enemy is in an adjacent position
        for x in range (len(enemyList)):
            Plr.gameLost(Dir.location, enemyList[x].enemyPos, Dir.Itm.hasWeapon(), Lab.labyrinth)
        #if an enemy is near the player the game ends
        if Plr.gameRunning == 0:
            print("Game lost!")
            print("Enemy caught you")
            for x in range (4):
                enemyList[x].printEnemyStatus()
            Plr.printStatus(Dir)
            return 
        #input command
        new_direction = input("Enter direction: ")
        os.system('cls')
        #help - prints the allowed commands
        if new_direction == "help":
            print("s, w, n ,e --> the location where you want to go")
            print("fight --> hit the enemy")
            print("quit --> stops the game forcefully")
            print("save --> saves the current state of the game")
            print("load --> loads a game saved previously")
            print("help --> prints the game commands")
        #quit stops the game regardless of its state
        elif new_direction == "quit":
            print("Game was stopped, the stas were:")
            for x in range (len(enemyList)):
                enemyList[x].printEnemyStatus()
            Plr.printStatus(Dir)
            return
        #saves the current state of the game
        elif new_direction == "save":
            Lab.uploadFile(Dir, Plr, enemyList, Lab)
            Plr.printStatus(Dir)
            print("New maze is: \n")
            Lab.printLabyrinth()
        #fight a nearby enemy
        elif new_direction == "fight":
            #note: we can't really know if an enemy is near the player so we have to check for each if we can fight
            for x in range (len(enemyList)):
               Plr.fight(enemyList[x], Dir, Lab.labyrinth)
            
            Plr.printStatus(Dir)
            print("New maze is: \n")
            Lab.printLabyrinth()
            
        else:
        #commands for the actual game
            Dir.move(new_direction, Lab.labyrinth)
            for x in range (len(enemyList)):
                enemyList[x].enemyMove(Lab.labyrinth)

            Plr.printStatus(Dir)
            print("New maze is: \n")
            Lab.printLabyrinth()


            
    #when while loop ends, there are 2 possibilities
    if Plr.gameRunning == 0:
        print("Game lost!")
        Plr.printStatus(Dir)
    else:
        print("Game won!")
        Plr.printStatus(Dir)
      
        
      
main()
