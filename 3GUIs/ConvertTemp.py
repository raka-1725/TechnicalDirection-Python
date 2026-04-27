# kelvin = celcius + 237.15

# fahrenheit = cel * 1.80 + 32.00

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QPushButton, QTextEdit

#conversions
def convert_temp_f(cdegree):
    return (float(cdegree) * 1.80) + 32.00

def convert_temp_k(cdegree):
    return float(cdegree) + 273.15

#ask user input for units
def ask_Input(input_temp):
    unit_choice = input("Input unit f/k/b : q to quit ").strip().lower()
    if unit_choice == 'f':
            print(f"{input_temp} is {convert_temp_f(input_temp)} F in Fahrenheit")
            return
    elif unit_choice == 'k':
            print(f"{input_temp} is {convert_temp_k(input_temp)} K in Kelvin")
            return
    elif unit_choice == 'b':
            print(f"{input_temp} is {convert_temp_f(input_temp)} F in Fahrenheit and {convert_temp_k(input_temp)} K in Kelvin")
            return
        #anything besides fkb will fall here and return None
    else :
            return
#main loop breaks when user inpiuts q
def main():
    while True:
        input_temp = input("Input temperature in celcius : q to quit ").strip().lower()
        if input_temp == "q":
            break
        ask_Input(input_temp)



class ConvertTemp(QMainWindow):
    def __init__(self):
        #initilize
        super().__init__()
        self.setWindowTitle("Temperature Converter")
        self.setMinimumWidth(500)

        #layout
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        #Input box
        layout.addWidget(QLabel("Input : "))
        self.Input = QTextEdit()
        self.Input.setMaximumHeight(50)
        self.Input.setPlaceholderText("Input Temperature here : ")
        layout.addWidget(self.Input)

        #buttons
        layout.addWidget(QLabel("Convert to : "))
        btn_row = QHBoxLayout()
        self.fah_btn = QPushButton("Fahrenheit")
        self.fah_btn.clicked.connect(self.do_convert_f)
        btn_row.addWidget(self.fah_btn)
        self.kel_btn = QPushButton("Kelvin")
        self.kel_btn.clicked.connect(self.do_convert_k)
        btn_row.addWidget(self.kel_btn)
        layout.addLayout(btn_row)


        #output
        layout.addWidget(QLabel("Result :"))
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("Convert result : ")
        layout.addWidget(self.output)

        self.output.append("=== Temperature Converter ===")
    
    #convert to F
    def do_convert_f(self):
        #convert to float
        tempInput = float(self.Input.toPlainText())
        result = convert_temp_f(tempInput)
        self.output.append(f"{tempInput} C in Celcius is {result} F in Fahrenheit.")
    #convert to K
    def do_convert_k(self):
        #convert to float
        tempInput = float(self.Input.toPlainText())
        result = convert_temp_k(tempInput)
        self.output.append(f"{tempInput} C in Celcius is {result} K in Kelvin.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConvertTemp()
    window.show()
    sys.exit(app.exec())