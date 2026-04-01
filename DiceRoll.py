import random


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


#constructor
if __name__ == "__main__":
    main()