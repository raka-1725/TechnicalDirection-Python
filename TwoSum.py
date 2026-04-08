#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def find_target(arr, target):
    for i in range(len(arr)):
       for j in range(i + 1, len(arr)):
           if arr[i] + arr[j] == target:
               return[i,j]
        



def main():
    while True:
        #Q to quit loop
        input_str = input("Input numbers for array: Q to quit").strip()
        if input_str in "Q" : 
            break
        inputTarget = input("Input target: Q to quit").strip()
        if inputTarget in "Q" : 
            break
        
        try:
            inputArr = [int(x) for x in input_str.split()]
        except ValueError:
            print("Please enter valid numbers.")
            continue

        result = find_target(inputArr, int(inputTarget))
        print(f"Input nums: {inputArr}, Result: {result}")



if __name__ == "__main__":
    main()