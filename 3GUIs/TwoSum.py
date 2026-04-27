#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QPushButton, QTextEdit

#run two for loops to add and find match with target
def find_target(arr, target):
    #initial loop
    n = len(arr)
    for i in range(n):
       #initial +  to find match
       for j in range(i + 1, n):
           #add to find match with target
           if arr[i] + arr[j] == target:
               #return and store two of index
               return[i,j]
        
def main():
    while True:
        #Q to quit loop
        input_str = input("Input numbers for array: Q to quit").strip()
        if input_str in "Q" : 
            break
        inputTarget = input("Input target: Q to quit").strip()
        if inputTarget in "Q" : 
            break
        #try and match
        try:
            #spliting input into array
            inputArr = [int(x) for x in input_str.split()]
        except ValueError:
            print("Please enter valid numbers.")
            continue
#get return array result from function
        result = find_target(inputArr, int(inputTarget))
        print(f"Input nums: {inputArr}, Result: {result}")

class TwoSum(QMainWindow):
    def __init__(self):
        #initilization
        super().__init__()
        self.setWindowTitle("Sum Finder")
        self.setMinimumWidth(500)
        #layout
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        #Array Input box
        layout.addWidget(QLabel("Input : "))
        self.InputArray = QTextEdit()
        self.InputArray.setMaximumHeight(50)
        self.InputArray.setPlaceholderText("Input Array here : ")
        layout.addWidget(self.InputArray)
        
        #Input box for Target
        layout.addWidget(QLabel("Target : "))
        self.InputTarget = QTextEdit()
        self.InputTarget.setMaximumHeight(50)
        self.InputTarget.setPlaceholderText("Input Target here : ")
        layout.addWidget(self.InputTarget)

        #button
        self.calc_btn = QPushButton("Find")
        self.calc_btn.clicked.connect(self.do_calc)
        layout.addWidget(self.calc_btn)

        #output
        layout.addWidget(QLabel("Result :"))
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("Calculation result : ")
        layout.addWidget(self.output)

        self.output.append("=== Two Sum Finder ===")

    def do_calc(self):
        #try splitting input into array
        try:
            InputStr = self.InputArray.toPlainText().replace(',', ' ').strip()
            InputArr = [int(x) for x in InputStr.split() if x.lstrip('-').isdigit()]
        except ValueError:
            self.output.append("Please enter valid numbers.")
        #convert target into int
        Target = int(self.InputTarget.toPlainText())
        result = find_target(InputArr, int(Target))

        self.output.append(f"Input nums: {InputArr}, Result: {result}")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TwoSum()
    window.show()
    sys.exit(app.exec())