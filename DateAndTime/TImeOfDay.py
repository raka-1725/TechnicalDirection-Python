#1. Allows the user to input a date
#2. Allows the user to ask what the date would be in x amount of days, months or years
#3. Format the user inputs accordingly and have the text in the terminal be clear and easy to read
#4. Comments on each function/clas


class DateCalculator:
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0

    def __str__(self):
        return f"{self.year} / {self.month} / {self.day}"

    
    def addDates(self, yearToAdd, monthToAdd, dayToAdd):
        print(yearToAdd, monthToAdd, dayToAdd)
        #add years
        self.year += yearToAdd

        #add month (12 > to increment year)
        self.month += monthToAdd

        while self.month > 12:
            self.month -= 12
            self.year += 1

        self.day += dayToAdd
        while True:
            #31 days
            if self.month in 1 or 3 or 5 or 7 or 8 or 10 or 12:
                while self.day > 31:
                    self.day -= 31
                    self.month += 1
            elif self.month == 4 or 6 or 9 or 11:
                while self.day > 30:
                    self.day - 30
                    self.month += 1
            else:
                if self.year % 4 == 0:
                    while self.day > 29:
                        self.day - 29
                        self.month += 1 
                else:
                    while self.day > 28:
                        self.day - 28
                        self.month += 1 

            if self.month > 12:
                self.month = 1
                self.year += 1
            else:
                break

    def printResult(self):
        print("=== Result Date ====")

        print(f"\n{self.year:04d} / {self.month:02d} / {self.day:02d}") 
        
    

    




def main():
    print("=== Calender Calculator ===\n")

    while True:
        dateCalc = DateCalculator()
        initial_month, initial_day, initial_year = input("Input Starting Date in MMDDYY format | eg: 04 15 2026\n").strip().split()

        dateCalc.year = initial_year
        dateCalc.month = initial_month
        dateCalc.day = initial_day

        print(dateCalc)

        print("\n==== Add ====")
        print("Adding offset: ")
        #try:
        year_offset = int(input("Input year offset : ")) or 0
        month_offset = int(input("Input month offset : ")) or 0
        day_offset = int(input("Input day offset : ")) or 0

        dateCalc.addDates(year_offset, month_offset, day_offset)

        dateCalc.printResult()

        calcAgain = input("Would you like to calculate again? (y/n)").strip().lower()
        if calcAgain is not "y":
            print("Quitting...")
            break
        #except:
            print("Invalid Input!")


if __name__ == "__main__":
    main()

