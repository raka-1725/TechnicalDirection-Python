# Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#Input: nums = [3,2,3] Output: 3

#find majority using median
def find_majority(arr):
    #sort array by order
    arr.sort()
    print(f"array {arr}")
    #divide by medium of array using len
    return arr[len(arr) // 2]

def main():
    while True:
        #Q to quit loop
        inputNum = input("Input numbers : Q to quit").strip()
        if inputNum in "Q" : 
            break

        try:
            #spliting input into array
            inputArr = [int(x) for x in inputNum.split()]
        except ValueError:
            print("Please enter valid numbers.")
            continue
    
        result = find_majority(inputArr)
        print(f"Majority number : {result}")


if __name__ == "__main__":
    main()

