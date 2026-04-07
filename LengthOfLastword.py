#Get the length of the last word
def get_last_word(word : str):
    #split words into list of string
    word_list = word.split()
    #return the last word in list
    return word_list[-1]

def main():
    while True:
        #q to quit
        input_str = input("Input string (Q to quit): ").strip()
        if input_str == "Q":
            break
        #get the last word from input
        lastWord = get_last_word(input_str)
        #get the word count of last word
        lastWordCount = len(lastWord)

        print(f"The last word of | {input_str} |  is : {lastWord} and length is {lastWordCount}")



if __name__ == "__main__":
    main()