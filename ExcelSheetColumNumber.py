#Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

#AA -> 27
#AB -> 28


#convert
def convert_to_num(input):
    # 'a' -> a(97) -> 1
    result = 0
    for char in input:
        # ord('A') = 65 
        value = ord(char) - 64
        # shift 26
        result = result * 26 + value
    return result


def main():
    while True:
        #Q to quit loop
        inputStr = input("Input alphabet to find column : 1 to quit ").strip().upper()
        if inputStr in "1" : 
            break
        #if it is not alphabet return
        if not inputStr.isalpha():
            print("Enter valid alphabetic characters.")
            continue
        
        resultNum = convert_to_num(inputStr)
        print(f"Column : {resultNum}")

if __name__ == "__main__":
    main()