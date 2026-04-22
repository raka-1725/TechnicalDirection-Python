# kelvin = celcius + 237.15

# fahrenheit = cel * 1.80 + 32.00





#conversions
def convert_temp_f(cdegree):
    return (float(cdegree) * 1.80) + 32.00

def convert_temp_k(cdegree):
    return float(cdegree) + 273.15

#ask user input for units
def ask_Input(input_temp):
    unit_choice = input("Input unit f/k/b : q to quit ").strip().lower()
    if unit_choice == 'f':
            print(f"{input_temp} is {convert_temp_f(input_temp)} F in Fahrenheit")
            return
    elif unit_choice == 'k':
            print(f"{input_temp} is {convert_temp_k(input_temp)} K in Kelvin")
            return
    elif unit_choice == 'b':
            print(f"{input_temp} is {convert_temp_f(input_temp)} F in Fahrenheit and {convert_temp_k(input_temp)} K in Kelvin")
            return
        #anything besides fkb will fall here and return None
    else:
            return
#main loop breaks when user inpiuts q
def main():
    while True:
        input_temp = input("Input temperature in celcius : q to quit ").strip().lower()
        if input_temp == "q":
            break
        ask_Input(input_temp)

        


if __name__ == "__main__":
    main()