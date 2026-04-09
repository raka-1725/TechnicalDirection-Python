#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.

#Input: nums = [2,2,1] Output: 1

#XOR operation
def find_single(arr):
    singleNum = 0
    n = len(arr)
    #loop through array
    for i in arr:
        #xor on single num comparing to i, when it is same turns value to 0, when it is diffeerent, adds up value
        # single ^= i
        print(f"single : {singleNum} || i : {i} | {singleNum ^ i}")
        singleNum = singleNum ^ i

    return singleNum



def main():
    while True:
        #Q to quit loop
        inputNum = input("Input numbers to find single number : Q to quit ").strip()
        if inputNum in "Q" : 
            break

        try:
            #spliting input into array
            inputArr = [int(x) for x in inputNum.split()]
        except ValueError:
            print("Please enter valid numbers.")
            continue

        result = find_single(inputArr)
        print(f"Single number : {result}")



if __name__ == "__main__":
    main()