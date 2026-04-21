import random
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QPushButton, QTextEdit

#score keeper for extra credit

playerInput = ""

#score keeper
playerwins = 0
playerLoses = 0
playerties = 0

bPlaying = False

def askPlayerChoice():
    print("Rock Sissor Paper game : Choose your choice : (Rock, Scissors, Paper)" )
    return input().strip().lower()

def decideComputerChoice():
    cpuChoice = random.randint(1, 3)
    #instead of match, it choses from these 3
    if cpuChoice == 1:
            return "rock"
    if cpuChoice == 2:
            return "paper"
    if cpuChoice == 3:
            return "scissors"

def battle():
    global playerwins, playerLoses, playerties

    computerChoice = decideComputerChoice()
    if computerChoice == "rock":
        if playerInput == "rock":
                playerties += 1
                print(f"You tied! : Ties {playerties}")
        elif playerInput == "scissors":
                playerLoses += 1
                print(f"You Lost! : Loses {playerLoses}")
        elif playerInput == "paper":
                playerwins += 1
                print(f"You won! : Wins {playerwins}")
        else:
                print("")
    elif computerChoice == "scissors":
        if playerInput == "scissors":
                playerties += 1
                print(f"You tied! : Ties {playerties}")
        elif playerInput == "paper":
                playerLoses += 1
                print(f"You Lost! : Loses {playerLoses}")
        elif playerInput == "rock":
                playerwins += 1
                print(f"You won! : Wins {playerwins}")
        else:
                print("")
    elif computerChoice == "paper":
        if playerInput == "scissors":
                playerties += 1
                print(f"You tied! : Ties {playerties}")
        elif playerInput == "paper":
                playerLoses += 1
                print(f"You Lost! : Loses {playerLoses}")
        elif playerInput ==  "rock":
                playerwins += 1
                print(f"You won! : Wins {playerwins}")
        else:
                print("")
    else:
        print("")


def printcurrentscore():
    print(f"Ties  | {playerties}")
    print(f"Wins  | {playerwins}")
    print(f"Loses | {playerLoses}")


if __name__ == "__main__":
        bPlaying = True
        while(bPlaying):
            playerInput = askPlayerChoice()
            battle()
            printcurrentscore()
            print("Type Q to stop game, C to continue game")
            if input().lower() == "q":
                bPlaying = False


        

