#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# n is the length of each array


def shuffleArray(arr, n):
#creating new array
    arrayShuffled = []
    #array for first half
    arrX = arr[:n]
    #array for second half
    arrY = arr[n:]

    #append to new array from array x and y using for loop from 0 to midpoint
    for i in range(n):
        arrayShuffled.append(arrX[i])
        arrayShuffled.append(arrY[i])

    return arrayShuffled


def main():
    while True:
        #input array
        inputNumsstr = input("Type array to shufflle, need space between numbers : Q to quit")
        if inputNumsstr == 'Q' : break
        #split array from string to int using split
        inputArr = [int(x) for x in inputNumsstr.split()]
        #getting the midpoint
        inputN = len(inputArr) // 2
        
        arr_result = shuffleArray(inputArr, inputN)
        print(f"arr_result {arr_result}")


if __name__ == "__main__":
    main()