#Given an integer num, return the number of digits in num that divide num. An integer val divides nums if nums % val == 0.

def is_divisible(number : int):
    #number to int
    numInt = int(number)
    #number to string from int
    digit_str = str(number)
    digitCount = 0
    #check if it can be devied by each digit
    for char in digit_str:
        #str to int
        digit = int(char)
        #if it is not 0 and divisible, add count
        if digit != 0 and numInt % digit == 0:
            digitCount += 1
        
    return digitCount

def main():
    while True:
        #Q to quit loop
        inputNum = input("Input numbers to devide by each digits: Q to quit").strip()
        if inputNum in "Q" : 
            break
        #try and exception for input
        try:
            val = int(inputNum)
            result = is_divisible(val)
            print(f"{val} is divisible by {result} digits.")


        except ValueError:
            print("Enter vaild numbers!!!")



if __name__ == "__main__":
    main()