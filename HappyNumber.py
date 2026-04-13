#A happy number is a number defined by the following process:

#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy. Return true if n is a happy number, and false if not.

# Input: n = 19
#Output: true
# Explanation: 12 + 92 = 82 | 82 + 22 = 68 |  62 + 82 = 100 | 12 + 02 + 02 = 1
def get_sum_square(n):
    total_sum = 0

    for digit in str(n): 
        total_sum += int(digit) ** 2
    return total_sum

#######

def is_happy(n):
    seen = set()
    # Keep going until n = 1 
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_sum_square(n)
    return n == 1

def happy_num_calc(n):
     
    return sum

def main():
    while True:
        #Q to quit loop
        inputNum = input("Input number to check if it is happy number : Q to quit ").strip()
        if inputNum in "Q" : 
            break

        try:
            #spliting input into array
            num = int(inputNum)
            if is_happy(num):
                print(f"{num} is happy number")
            else:
                print(f"{num} is NOT happy number")
       
        except ValueError:
            print("Please enter valid numbers.")
            continue
        
        #print(f"Is {inputNum} happy number? : {is_happy(inputNum)}")

if __name__ == "__main__":
    main()