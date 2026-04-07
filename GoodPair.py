#Given an array of integers nums, return the number of good pairs. A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def is_good_pair(input):
    count = 0
    #length of array
    n = len(input)
    #index i
    for i in range(n):
        #index j (+1 to i, run until it reaches end of array)
        for j in range(i + 1, n):
            #if it matches, increment count
            if input[i] == input[j]:
                count += 1
    return count

def main():
    while True:
        inputNums = input("Input the array ")

        #split array from string to array
        nums = [int(x) for x in inputNums.split()]
        #get count of good array
        result = is_good_pair(nums)
        #print
        print(f"Number of good pairs: {result}")

if __name__ == "__main__":
    main()