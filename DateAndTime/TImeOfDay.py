#1. Allows the user to input a date
#2. Allows the user to ask what the date would be in x amount of days, months or years
#3. Format the user inputs accordingly and have the text in the terminal be clear and easy to read
#4. Comments on each function/clas


class Date:
    def __init__(self, year, month, day):
        self.years = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.years} {self.month} {self.day}"
    
def GetDiff(Date_Initial, Date_Target):
    day_diff = 0
    month_diff = 0
    year_diff = 0

    




def main():
    print("=== Calender Calculator ===\n")

    while True:

        initial_month, initial_day, initial_year = input("Input Starting Date in MMDDYY format | eg: 04 15 2026\n").strip().split()
        Initial_date = Date(initial_year, initial_month, initial_day)

        print(f"Inital date : {Initial_date}")

        target_month, target_day, target_year = input("\nInput Target Date in MMDDYY format | eg: 04 15 2026\n").strip().split()
        Target_date = Date(target_year, target_month, target_day)

        print(f"Target date : {Target_date}")


if __name__ == "__main__":
    main()

