
#Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.  



#replace with empty for letters that returned as true
def remove_vowels(input_str):
    #replace empty if it is vowel
    return "".join(x for x in input_str if not is_vowel(x))

    return new_string

#return false if the letter is vowel
def is_vowel(letter):
    #check if the letter is vowel
    return letter.lower() in "aeiou"

def main():
    while True:
        #q to quit
        input_str = input("Input string (Q to quit): ").strip()
        if input_str == "Q":
            break
        #gets removed string
        result = remove_vowels(input_str)
        print("Result:", result)



if __name__ == "__main__":
    main()