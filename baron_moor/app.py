#!/usr/bin/env python3

import random
from CalculatePosition import *
from Dial import Dial 
from GameBoard import * 
from HiddenTreasures import *
from Movement import *
from Navigation import * 
from PlayerPosition import *
from Trap import *
from TreasurePosition import *
from time import sleep

def main():

    viewing = None
    option = None
    toGo = None
    toGoCondition = True
    playerXPosition = None
    playerYPosition = None
    treasureXPosition = None
    treasureYPosition = None
    hiddenXPosition = None
    hiddenYPosition = None
    trapX = None
    trapY = None
    con = True
    positionMatching = True

    print("""
 █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████                                                                                             """)
    sleep(0.1)
    print(
"""▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀                                                                                             """)
    sleep(0.1)
    print(
"""▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███                                                                                               """)
    sleep(0.1)
    print(
"""░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄                                                                                             """)
    sleep(0.1)
    print(
"""░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒                                                                                            """)
    sleep(0.1)
    print(
"""░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░                                                                                            """)
    sleep(0.1)
    print(
"""  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░                                                                                            """)
    sleep(0.1)
    print(
"""  ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░                                                                                               """)
    sleep(0.1)
    print(
"""    ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░                                                                                            """)
    sleep(0.1)
    print(
"""                        ░                                                                                                                               """)
    sleep(0.1)
    print(
"""                                    ▄▄▄█████▓ ▒█████      ▄▄▄▄    ▄▄▄       ██▀███   ██▀███  ▓█████  ███▄    █     ███▄ ▄███▓ ▒█████   ▒█████   ██▀███  """)
    sleep(0.1)
    print(
"""                                    ▓  ██▒ ▓▒▒██▒  ██▒   ▓█████▄ ▒████▄    ▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀  ██ ▀█   █    ▓██▒▀█▀ ██▒▒██▒  ██▒▒██▒  ██▒▓██ ▒ ██▒""")
    sleep(0.1)
    print(
""""                                    ▒ ▓██░ ▒░▒██░  ██▒   ▒██▒ ▄██▒██  ▀█▄  ▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▓██  ▀█ ██▒   ▓██    ▓██░▒██░  ██▒▒██░  ██▒▓██ ░▄█ ▒""")
    sleep(0.1)
    print(
"""                                    ░ ▓██▓ ░ ▒██   ██░   ▒██░█▀  ░██▄▄▄▄██ ▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▓██▒  ▐▌██▒   ▒██    ▒██ ▒██   ██░▒██   ██░▒██▀▀█▄  """)
    sleep(0.1)
    print(
"""                                      ▒██▒ ░ ░ ████▓▒░   ░▓█  ▀█▓ ▓█   ▓██▒░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒██░   ▓██░   ▒██▒   ░██▒░ ████▓▒░░ ████▓▒░░██▓ ▒██▒""")
    sleep(0.1)
    print(
"""                                      ▒ ░░   ░ ▒░▒░▒░    ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ▒ ▒    ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░""")
    sleep(0.1)
    print(
"""                                        ░      ░ ▒ ▒░    ▒░▒   ░   ▒   ▒▒ ░  ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░░ ░░   ░ ▒░   ░  ░      ░  ░ ▒ ▒░   ░ ▒ ▒░   ░▒ ░ ▒░""")
    sleep(0.1)
    print(
"""                                      ░      ░ ░ ░ ▒      ░    ░   ░   ▒     ░░   ░   ░░   ░    ░      ░   ░ ░    ░      ░   ░ ░ ░ ▒  ░ ░ ░ ▒    ░░   ░ """)
    sleep(0.1)
    print(
"""                                                 ░ ░      ░            ░  ░   ░        ░        ░  ░         ░           ░       ░ ░      ░ ░     ░     
    """)
    sleep(0.1)
    board_choice = input("Play with a standard board? [Y/N]: ").lower()
    sleep(0.1)
    playerPosition = PlayerPosition()
    treasurePosition = TreasurePosition()
    hiddenTreasures = HiddenTreasures()
    trap = Trap()

    while board_choice != "y" and board_choice != "n":
        board_choice = input("Please enter 'Y' or 'N': ").lower()
        sleep(0.1)
    if board_choice == 'n':
        board_choice_y = input("How wide should the board be? [Enter integer]: ")
        sleep(0.1)
        while board_choice_y.isnumeric() == False:
            board_choice_y = input("Please enter an integer: ")
            sleep(0.1)
        board_choice_y = int(board_choice_y)
        board_choice_x = input("How tall should the board be? [Enter integer]: ")
        sleep(0.1)
        while board_choice_x.isnumeric() == False:
            board_choice_x = input("Please enter an integer: ")
            sleep(0.1)
        board_choice_x = int(board_choice_y)
        playerPosition.gb.setRows(board_choice_x)
        playerPosition.gb.setColumns(board_choice_y)
        treasurePosition.gb.setRows(board_choice_x)
        treasurePosition.gb.setColumns(board_choice_y)
        hiddenTreasures.gb.setRows(board_choice_x)
        hiddenTreasures.gb.setColumns(board_choice_y)
        trap.gb.setRows(board_choice_x)
        trap.gb.setColumns(board_choice_y)
    
    while con:
        print("You awaken to find yourself in a barren moor. Try \"look\"")
        sleep(0.1)
        viewing = input().lower()

        if viewing == "look":
            print("Grey foggy clouds float oppressively close to you,")
            sleep(0.1)
            print("reflected in the murky grey water which reaches up your shins.")
            sleep(0.1)
            print("Some black plants barely poke out of the shallow water.")
            sleep(0.1)
            con = False
        else:
            print("You have entered an incorrect statement, \n" +
                        "do you wish to exit the viewing?, \n" +
                        "Please enter either \"Yes\" or \"No\"")
            sleep(0.1)

            option = input().lower()

            if option == "yes":
                con = False

            else:
                pass

    playerXPosition = playerPosition.calculateXPosition()
    playerYPosition = playerPosition.calculateYPosition()
    treasureXPosition = treasurePosition.calculateXPosition()
    treasureYPosition = treasurePosition.calculateYPosition()
    hiddenTXPosition = hiddenTreasures.calculateXPosition()
    hiddenTYPosition = hiddenTreasures.calculateYPosition()
    trapX = trap.calculateXPosition()
    trapY = trap.calculateYPosition()


    while positionMatching:
        
        if (playerXPosition == treasureXPosition or playerYPosition == treasureYPosition 
        or hiddenTXPosition == playerXPosition or hiddenTYPosition == playerYPosition 
        or hiddenTXPosition == treasureXPosition or hiddenTYPosition == treasureYPosition 
        or trapX == playerXPosition or trapY == playerYPosition):
            
            playerXPosition = playerPosition.calculateXPosition()
            playerYPosition = playerPosition.calculateYPosition()
            treasureXPosition = treasurePosition.calculateXPosition()
            treasureYPosition = treasurePosition.calculateYPosition()
            hiddenTXPosition = hiddenTreasures.calculateXPosition()
            hiddenTYPosition = hiddenTreasures.calculateYPosition()
            trapX = trap.calculateXPosition()
            trapY = trap.calculateYPosition()

        else:
            positionMatching = False

    navigation = Navigation(playerXPosition, playerYPosition, treasureXPosition, treasureYPosition)

    dial = Dial()

    print("Try \"North\", \"South\", \"East\" or \"West\"")
    sleep(0.1)
    print("You notice a small watch-like device in your left hand.")
    sleep(0.1)
    print("It has hands like a watch, but the hands don’t seem to tell")
    sleep(0.1)
    print("The dial reads " + str(navigation.calculateResultant()) + "m")
    sleep(0.1)

    while toGoCondition:

        if playerXPosition == hiddenTXPosition and playerYPosition == hiddenTYPosition:
            print("You have discovered the legendary EI sword to aid you in your quest")
            sleep(0.1)
        
        if trapX == playerXPosition and trapY == playerYPosition:
            print("You fell into a trap, you're dead now")
            sleep(2)
            toGoCondition = False

        if playerXPosition == treasureXPosition and playerYPosition == treasureYPosition:
            print("You found the treasure, now go save the world. THE END")
            sleep(2)
            toGoCondition = False
        
        else:
            
            toGo = input("Please enter directions to go: ").lower()
            sleep(0.1)

            if toGo == "north" or toGo == "n":
                playerYPosition = dial.north(playerYPosition)
                navigation.setpY(playerYPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
                sleep(0.1)
            elif toGo == "east" or toGo == "e":
                playerXPosition = dial.east(playerXPosition)
                navigation.setpX(playerXPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
                sleep(0.1)
            elif toGo == "south" or toGo == "s":
                playerYPosition = dial.south(playerYPosition)
                navigation.setpY(playerYPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
                sleep(0.1)
            elif toGo == "west" or toGo == "w":
                playerXPosition = dial.west(playerXPosition)
                navigation.setpX(playerXPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
                sleep(0.1)
            else:
                print("You havent chosen a direction to go")
                sleep(0.1)
                print(navigation.calculateResultant())
            
if __name__ == "__main__":
    main()