#Given an integer x, return true if x is a  palindrome, and false otherwis

#checking if it is palindrome
def is_Palindrome(nums):
    #comparing in string, with the other string that is converted backwards using [::-1]
    return str(nums) == str(nums)[::-1]

def main():
    while True:
        #q to quit
        input_num = input("Input string | (Q to quit): ").strip()
        if input_num == "Q":
            break
        #print and calling function
        print(f"{input_num} is Palindrome? {is_Palindrome(input_num)}")



if __name__ == "__main__":
    main()