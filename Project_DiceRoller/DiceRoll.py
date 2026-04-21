import random
import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QPushButton, QTextEdit

#get random int using random
def roll_die(sides):
    return random.randint(1,sides)

#execute roll_dice() for count using for loop
def roll_dice(count, sides):
    return[roll_die(sides) for _ in range(count)]

def choose_sides():
    print("Enter the number of sides for the dice you want to roll.")
    print("Type Q to quit")
    
#While loop for asking sides, exits when q entered
    while True:
        choice = input("How many sides does the dice have").strip().lower()
        if choice == "q" :
            return None
        if not choice.isdigit() or int(choice) < 2:
            print("Invaild Input !!!! Enter value grater than 2 : Press Q to quit")
            continue
        return int(choice)

#While loop for asking counts, exits when q entered
def choose_count():
    while True:
        amount = input("How many dice do you want to roll?").strip().lower()
        if amount == "q":
            return None
        if not amount.isdigit() or int(amount) < 1:
            print("Invaild Input!!! Enter value more than 1 : Press Q to quit")
            continue
        return int(amount)

#asking re-roll
def ask_reroll():
    while True:
        answer = input("Would you like to Reroll??? (y/n) : ").strip().lower()
        if answer in ("y","yes"):
            return True
        if answer in ("n","no"):
            return False
        print("Please enter y or n")
            
#detects 1 or 20 in d20 dices
def report_naturals(result, sides):
    if sides != 20:
        return  
    if 1 in result:
        print("Try better next time. : Natual 1")
    if 20 in result:
        print("You spend all of your luck : Natural 20")

def main():
    print("Dice Roller V 1.0")
    while True:
        #if return is None break from loop
        sides = choose_sides()
        if sides is None:
            break
        count = choose_count()
        if count is None : 
            break
#take count and sides and rolls dice
        result = roll_dice(count, sides)
        #print result usin for loop
        print(f"You rolled {count} d{sides}(s) : {', '.join(str(r) for r in result)}")
        print(f"Total : {sum(result)}\n")
        report_naturals(result, sides)

        while ask_reroll(): 
            result = roll_dice(count, sides)
            #print result usin for loop
            print(f"Reroll result: {', ' .join(str(r) for r in result)}")
            print(f"New Total : {sum(result)}\n")
            report_naturals(result, sides)

    print("Thanks for rolling")

class DiceRollerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DiceRoller")
        self.setMinimumWidth(420)

        self.last_sides = None
        self.last_count = None
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        #Num of sides
        sides_row = QHBoxLayout()
        sides_row.addWidget(QLabel("Number of sides (2 or more)"))
        self.sides_spin = QSpinBox()
        self.sides_spin.setMinimum(2)
        self.sides_spin.setMaximum(1000)
        self.sides_spin.setValue(10)
        sides_row.addWidget(self.sides_spin)
        layout.addLayout(sides_row)

        #Count
        count_row = QHBoxLayout()
        count_row.addWidget(QLabel("Number of dice (1 or more)"))
        self.count_spin = QSpinBox()
        self.count_spin.setMinimum(1)
        self.count_spin.setMaximum(100)
        self.count_spin.setValue(20)
        count_row.addWidget(self.count_spin)
        layout.addLayout(count_row)

        #Buttons
        btn_row = QHBoxLayout()
        self.roll_btn = QPushButton("Roll")
        self.roll_btn.clicked.connect(self.do_roll)
        self.re_roll_btn = QPushButton("Re-Roll")
        self.re_roll_btn.clicked.connect(self.do_reroll)
        self.re_roll_btn.setEnabled(False)
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.do_clear)
        btn_row.addWidget(self.roll_btn)
        btn_row.addWidget(self.re_roll_btn)
        btn_row.addWidget(self.clear_btn)
        layout.addLayout(btn_row)


        #Output
        layout.addWidget(QLabel("Results:"))
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("Roll Result : ")
        layout.addWidget(self.output)

        self.output.append("=== Dice Roller === \n Enter sides and count, then press Roll")

    def do_roll(self):
        self.last_sides = self.sides_spin.value()
        self.last_count = self.count_spin.value()
        self._roll_and_display(self.last_sides, self.last_count, reroll = False)
        self.re_roll_btn.setEnabled(True)
    
    def do_reroll(self):
        self._roll_and_display(self.last_sides, self.last_count, reroll = True)

    def do_clear(self):
        self.output.clear()
    
    def _roll_and_display(self, sides, count, reroll):
        results = roll_dice(count, sides)
        label = "Re-Roll" if reroll else f"Rolled {count}d{sides}"
        self.output.append(f"{label} : {', '.join(str(r) for r in results)}")
        self.output.append(f"Total : {sum(results)}")
        if sides == 20:
            if 1 in results:
                self.output.append("Try better next time. : Natual 1")
            if 20 in results:
                self.output.append("You spend all of your luck : Natural 20")
        self.output.append("")

#constructor
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiceRollerWindow()
    window.show()
    sys.exit(app.exec())
