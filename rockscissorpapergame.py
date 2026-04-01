import random

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
    match cpuChoice:
        case 1:
            return "rock"
        case 2:
            return "paper"
        case 3:
            return "scissors"

def battle():
    global playerwins, playerLoses, playerties

    computerChoice = decideComputerChoice()
    if computerChoice == "rock":
        match playerInput:
            case "rock":
                playerties += 1
                print(f"You tied! : Ties {playerties}")
            case "scissors":
                playerLoses += 1
                print(f"You Lost! : Loses {playerLoses}")
            case "paper":
                playerwins += 1
                print(f"You won! : Wins {playerwins}")
            case _:
                print("")
    elif computerChoice == "scissors":
        match playerInput:
            case "scissors":
                playerties += 1
                print(f"You tied! : Ties {playerties}")
            case "paper":
                playerLoses += 1
                print(f"You Lost! : Loses {playerLoses}")
            case "rock":
                playerwins += 1
                print(f"You won! : Wins {playerwins}")
            case _:
                print("")
    elif computerChoice == "paper":
        match playerInput:
            case "scissors":
                playerties += 1
                print(f"You tied! : Ties {playerties}")
            case "paper":
                playerLoses += 1
                print(f"You Lost! : Loses {playerLoses}")
            case "rock":
                playerwins += 1
                print(f"You won! : Wins {playerwins}")
            case _:
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


        

