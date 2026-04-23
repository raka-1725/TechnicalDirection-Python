#Given an integer x, return true if x is a  palindrome, and false otherwis
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QPushButton, QTextEdit

#checking if it is palindrome
def is_Palindrome(nums):
    #comparing in string, with the other string that is converted backwards using [::-1]
    return str(nums) == str(nums)[::-1]

def main():
    while True:
        #q to quit
        input_num = input("Input string | (Q to quit): ").strip()
        if input_num == "Q":
            break
        #print and calling function
        print(f"{input_num} is Palindrome? {is_Palindrome(input_num)}")

class PalindromeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Palindrome Checker")
        self.setMinimumWidth(500)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        #Input text box
        layout.addWidget(QLabel("Input : "))
        self.Input = QTextEdit()
        self.Input.setMaximumHeight(50)
        self.Input.setPlaceholderText("Input word here : ")
        layout.addWidget(self.Input)

        #execute button
        self.check_btn = QPushButton("Check")
        layout.addWidget(self.check_btn)

        #output
        layout.addWidget(QLabel("Result : "))
        self.Output = QTextEdit()
        self.Output.setMaximumHeight(50)
        self.Output.setReadOnly(True)
        self.Output.setPlaceholderText("Is it Palindrome? : ")
        layout.addWidget(self.Output)
        
        #connect button
        self.check_btn.clicked.connect(self.check_palindrome)

    def check_palindrome(self):
        text = self.Input.toPlainText()
        result = is_Palindrome(text)

        if result == True:
            self.Output.append(f"{text} is Palindrome")
        else:
            self.Output.append(f"{text} is Not Palindrome")



        
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PalindromeWindow()
    window.show()
    sys.exit(app.exec())