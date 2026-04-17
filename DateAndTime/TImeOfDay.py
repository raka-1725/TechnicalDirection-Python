#1. Allows the user to input a date
#2. Allows the user to ask what the date would be in x amount of days, months or years
#3. Format the user inputs accordingly and have the text in the terminal be clear and easy to read
#4. Comments on each function/clas


class DateCalculator:
    #constructor : initilizing dates
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0
    #print : returns f string when the print calls this functions
    def __str__(self):
        return f"{self.year} / {self.month} / {self.day}"

    #adding date with increment day, year, month
    def addDates(self, yearToAdd, monthToAdd, dayToAdd):
        #print(yearToAdd, monthToAdd, dayToAdd)
        #add years
        self.year += yearToAdd

        #add month (12 > to increment year)
        self.month += monthToAdd

        #increment year when the month sum is > 12
        while self.month > 12:
            self.month -= 12
            self.year += 1
        
        #adding days
        self.day += dayToAdd
        #adding days with proper increment
        while True:
            #31 days
            if self.month in [1,3,5,7,8,10,12]:
                daysLimit = 31
            #30 days
            elif self.month in [4,6,9,11]:
                daysLimit = 30
            #Febuary
            else:
                #feburary leap year
                if self.year % 4 == 0:
                    daysLimit = 29
                #feburary NON leap year
                else:
                    daysLimit = 28
            #increment month based on the days limit
            if self.day > daysLimit:
                self.day -= daysLimit
                self.month += 1
            #increment year if the month becomes more than 12
                if self.month > 12:
                    self.month = 1
                    self.year += 1
            #break from loop
            else:
                break
    #print result with digit format
    def printResult(self):
        print("\n=== Result Date ====")
        print(f"{self.year:04d} / {self.month:02d} / {self.day:02d}")
        
    

    




def main():
    print("=== Calender Calculator ===\n")

    while True:
        try:
            #Instantiating function
            dateCalc = DateCalculator()
            #asking user input
            InitialInput = input("Input Starting Date in MM DD YYYY format | eg: 04 15 2026\n").strip().split()
            #if the input is not array of 3 (day month year) show error
            if len(InitialInput) != 3:
                    print("Error: Please enter three numbers separated by space")
                    continue
            #setting input on the class
            dateCalc.year = int(InitialInput[2])
            dateCalc.month = int(InitialInput[0])
            dateCalc.day = int(InitialInput[1])
            #show the inital date
            print(f"Starting Date : {dateCalc}")

            print("\n==== Add ====")
            print("Adding offset: ")
            #Asking user offset input
            year_offset = int(input("Input year offset : ")) or 0
            month_offset = int(input("Input month offset : ")) or 0
            day_offset = int(input("Input day offset : ")) or 0
            #Call function to add dates
            dateCalc.addDates(year_offset, month_offset, day_offset)
            #print the result of adding offsets
            dateCalc.printResult()
        except:
            print("Invalid Input!")
            continue

        #Asking user want to calculate again
        calcAgain = input("\nWould you like to calculate again? (y/n): ").strip().lower()
        #if the input is not y, break from loop
        if calcAgain != "y":
            print("Quitting...")
            break


if __name__ == "__main__":
    main()

