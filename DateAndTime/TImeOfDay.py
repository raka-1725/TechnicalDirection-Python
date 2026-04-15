#1. Allows the user to input a date
#2. Allows the user to ask what the date would be in x amount of days, months or years
#3. Format the user inputs accordingly and have the text in the terminal be clear and easy to read
#4. Comments on each function/clas


class date:
    def __init__(self, year, month, day):
        self.years = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.years} {self.month} {self.day}"
    

def main():
    print("=== Calender Calculator ===\n")

    while True:

        initial_date = input("\nInput Starting Date in MMDDYY format | eg: APR 15 2026").strip()
