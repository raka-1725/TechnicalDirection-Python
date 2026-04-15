from datetime import datetime
import zoneinfo

class TimeOfDay:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __repr__(self):
        return f"TimeOfDay({self.hours}, {self.minutes}, {self.seconds})"

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    @classmethod
    def from_timezone(cls, timezone_name):
        tz = zoneinfo.ZoneInfo(timezone_name)
        now = datetime.now(tz)
        return cls(now.hour, now.minute, now.second)

    def __add__(self, other):
        total = self.to_seconds() + other.to_seconds()
        return TimeOfDay.from_seconds(total % 86400)

    def __sub__(self, other):
        total = (self.to_seconds() - other.to_seconds()) % 86400
        return TimeOfDay.from_seconds(total)

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()


#Hours to add to Central Time to reach each timezone (standard offsets)
#Positive = ahead of Central, Negative = behind Central
TIMEZONE_OFFSETS = {
    "1": ("Eastern",         +1),
    "2": ("Mountain",        -1),
    "3": ("Pacific",         -2),
    "4": ("Alaska",          -3),
    "5": ("Hawaii",          -4),
    "6": ("London (GMT)",    +6),
    "7": ("Paris (CET)",     +7),
    "8": ("Moscow",          +9),
    "9": ("Dubai",           +10),
    "10": ("India",          +11),  
    "11": ("Tokyo",          +15),
    "12": ("Sydney",         +16),
}


def format_12hr(hour, minute):
    #Convert 24-hour hour/minute to a 12-hour AM/PM string.
    period = "AM" if hour < 12 else "PM"
    display_hour = hour % 12
    if display_hour == 0:
        display_hour = 12
    return f"{display_hour}:{minute:02d} {period}"


def get_user_time():
    #Prompt the user to enter a time in Central Time and return the hour and minute.
    while True:
        time_str = input("Enter a time in Central Time (e.g. 3:45 PM or 11:05 AM): ").strip()
        try:
            dt = datetime.strptime(time_str, "%I:%M %p")
            return dt.hour, dt.minute
        except ValueError:
            try:
                dt = datetime.strptime(time_str, "%I %p")
                return dt.hour, dt.minute
            except ValueError:
                print("  Invalid format. Please use h:mm AM/PM (e.g. 3:45 PM).\n")


def pick_destination():
    #Prompt the user to pick a destination timezone.
    print("\nAvailable timezones to convert to:")
    for key, (label, offset) in TIMEZONE_OFFSETS.items():
        sign = "+" if offset >= 0 else ""
        print(f"  {key:>2}. {label:<20} (Central {sign}{offset} hrs)")
    while True:
        choice = input("\nEnter number: ").strip()
        if choice in TIMEZONE_OFFSETS:
            return TIMEZONE_OFFSETS[choice]
        print("  Invalid choice, please try again.")


def convert_and_display(central_hour, minute, dest_label, offset):
    #Apply the offset and print the conversion result.
    central_display = format_12hr(central_hour, minute)
    central_time = TimeOfDay(central_hour, minute, 0)
    offset_time = TimeOfDay(abs(offset), 0, 0)

    if offset >= 0:
        dest_time = central_time + offset_time
    else:
        dest_time = central_time - offset_time

    dest_display = format_12hr(dest_time.hours, dest_time.minutes)
    sign = "+" if offset >= 0 else "-"
    print(f"\n  Central Time:     {central_display}")
    print(f"  Offset applied:   {sign}{abs(offset)} hour(s)")
    print(f"  {dest_label + ':':18} {dest_display}")


def main():
    #Main function for converting Central Time to other timezones
    print("=== Central Time Zone Converter ===\n")

    while True:
        #Step 1: get the time in Central Time
        central_hour, minute = get_user_time()

        #Step 2: pick destination timezone
        dest_label, offset = pick_destination()

        #Step 3: convert and display
        convert_and_display(central_hour, minute, dest_label, offset)

        #Step 4: ask to continue
        again = input("\nWould you like to convert another time? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nGoodbye!")
            break
        print()
#1. Allows the user to input a date
#2. Allows the user to ask what the date would be in x amount of days, months or years
#3. Format the user inputs accordingly and have the text in the terminal be clear and easy to read
#4. Comments on each function/clas








if __name__ == "__main__":
    main()