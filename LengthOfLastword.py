#Get the length of the last word
def get_last_word(word : str):
    word_list = word.split()
    return word_list[-1]

def main():
    while True:
        #q to quit
        input_str = input("Input string (Q to quit): ").strip()
        if input_str == "Q":
            break
        
        lastWord = get_last_word(input_str)
        lastWordCount = len(lastWord)

        print(f"The last word of | {input_str} |  is : {lastWord} and length is {lastWordCount}")



if __name__ == "__main__":
    main()