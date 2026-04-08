
def main():
    while True:
        #Q to quit loop
        inputNum = input("Input numbers to devide by each digits: Q to quit").strip()
        if inputNum in "Q" : 
            break



if __name__ == "__main__":
    main()

#---------------------------------------------------------------------------

    inputArr = [int(x) for x in inputNumsstr.split()]
    #getting the midpoint
    inputN = len(inputArr) 