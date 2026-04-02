
#Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.  




def remove_vowels(input_str):
    new_string = input_str
    for x in input_str:
        if is_vowel(x):
            x.replace(f"{x}", "")

    return new_string

def is_vowel(letter):

    if letter == 'a':
        return True
    elif letter == 'e':
        return True
    elif letter == 'i':
        return True
    elif letter == 'o':
        return True
    elif letter == 'u':
        return True
    else:
        return False

def main():
    while True:
        stones = input("Input stones : Q to quit").strip()
        if stones in "Q" : 
            break
        result = check_stone(stones, jewels)

        print(f"You have {result} jewels in your stones")


if __name__ == "__main__":
    main()