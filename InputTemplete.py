
def main():
    while True:
        #Q to quit loop
        inputNum = input("Input numbers : Q to quit ").strip()
        if inputNum in "Q" : 
            break

        try:
            #spliting input into array
            inputArr = [int(x) for x in inputNum.split()]
        except ValueError:
            print("Please enter valid numbers.")
            continue

        result = FUNCTION(inputArr)
        print(f"Result number : {result}")



if __name__ == "__main__":
    main()
#---------------------------------------------------------------------------

    inputArr = [int(x) for x in inputNumsstr.split()]
    #getting the midpoint
    inputN = len(inputArr) 