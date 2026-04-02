
#find jewel letter from stone string
#ex: aaBBBaAA -> Jewel->aA : output 3

#jewels

jewels = "Abtj"

# check each letter will match in the jewels using two for loops
def check_stone(stone, jewels):
    hitresult = 0
    for x in stone:
        for y in jewels:
            if x == y:
                hitresult += 1
    #returns int of how many time it matched
    return hitresult


#main loops
def main():
    while True:
        #Q to quit loop
        stones = input("Input stones : Q to quit").strip()
        if stones in "Q" : 
            break
        #get result of checking stone
        result = check_stone(stones, jewels)
        
        print(f"You have {result} jewels in your stones")


if __name__ == "__main__":
    main()