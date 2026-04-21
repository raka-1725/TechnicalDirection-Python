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
                return(f"CPU choice : {computerChoice} \nYou tied! : Ties {playerties}")
        elif playerInput == "scissors":
                playerLoses += 1
                return(f"CPU choice : {computerChoice} \nYou Lost! : Loses {playerLoses}")
        elif playerInput == "paper":
                playerwins += 1
                return(f"CPU choice : {computerChoice} \nYou won! : Wins {playerwins}")
        else:
                return("")
    elif computerChoice == "scissors":
        if playerInput == "scissors":
                playerties += 1
                return(f"CPU choice : {computerChoice} \nYou tied! : Ties {playerties}")
        elif playerInput == "paper":
                playerLoses += 1
                return(f"CPU choice : {computerChoice} \nYou Lost! : Loses {playerLoses}")
        elif playerInput == "rock":
                playerwins += 1
                return(f"CPU choice : {computerChoice} \nYou won! : Wins {playerwins}")
        else:
                return("")
    elif computerChoice == "paper":
        if playerInput == "scissors":
                playerties += 1
                return(f"CPU choice : {computerChoice} \nYou tied! : Ties {playerties}")
        elif playerInput == "paper":
                playerLoses += 1
                return(f"CPU choice : {computerChoice} \nYou Lost! : Loses {playerLoses}")
        elif playerInput ==  "rock":
                playerwins += 1
                return(f"CPU choice : {computerChoice} \nYou won! : Wins {playerwins}")
        else:
                return("")
    else:
        return("")


def printcurrentscore():
    return(f"Ties  | {playerties} \n Wins  | {playerwins} \n Loses | {playerLoses}")


class RSPWindow(QMainWindow):
        def __init__(self):
                super().__init__()
                self.setWindowTitle("Rock Paper Scissors game")
                self.setMinimumWidth(500)


                central = QWidget()
                self.setCentralWidget(central)
                layout = QVBoxLayout(central)

                #player input button
                btn_row = QHBoxLayout()
                self.rock_btn = QPushButton("Rock")
                self.rock_btn.clicked.connect(self.send_rock)
                self.paper_btn = QPushButton("Paper")
                self.paper_btn.clicked.connect(self.send_paper)
                self.scissors_btn = QPushButton("Scissors")
                self.scissors_btn.clicked.connect(self.send_scissors)
                btn_row.addWidget(self.rock_btn)
                btn_row.addWidget(self.paper_btn)
                btn_row.addWidget(self.scissors_btn)
                layout.addLayout(btn_row)

                #output
                layout.addWidget(QLabel("Result : "))
                self.output = QTextEdit()
                self.output.setReadOnly(True)
                self.output.setPlaceholderText("Game Result : ")
                layout.addWidget(self.output)


                self.output.append("=== Rock Paper Scissors Game === \nPress your choice")

        def send_rock(self):
               global playerInput
               playerInput = "rock"
               self.display_result(playerInput)
        def send_paper(self):
               global playerInput
               playerInput = "paper"
               self.display_result(playerInput)
        def send_scissors(self):
               global playerInput
               playerInput = "scissors"
               self.display_result(playerInput)


        
        def display_result(self, choice):
               global playerInput
               playerInput = choice
               self.output.append(f"Your choice : {playerInput}")
               self.output.append(battle())
               self.output.append(printcurrentscore())










if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RSPWindow()
    window.show()
    sys.exit(app.exec())


        

