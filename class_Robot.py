class Robot:

    #constr
    def __init__(self, name: str, color: str, weight: float, purpose: str):
        self.name = name
        self.color = color
        self.weight = weight
        self.purpose = purpose
        
        # -> is return type
    def display_info(self) -> None:
        print(f"Hello World! I am : {self.name} and {self.color} robot, weighting {self.weight} kg. My purpose is {self.purpose}")
        

if __name__ == "__main__":
    robots = {}
    
    while True:
        print("\n-- Robot Factory ---")
        print("1. Add a new robot")
        print("2. View a robot by name")
        print("3. Override an existing robot")
        print("4. Exit")
        
        choice = input("Enter your choice : ")

        if choice == "1":
            name = input("Enter Robot's name : ")

            if name in robots: 
                overwrite = input(f"A robot named {name} already exits! Overwrite it? (y/n)").strip().lower()
                if overwrite != "y":
                    print("Robot not added")
                    continue
                
            color = input("Enter Robot's color: ")

            while True:
                try:
                    weight = float(input("Enter robot's weight: "))
                    break
                except ValueError:
                    print("Invalid Input! Enter a number for weight.")


            purpose = input("Enter Robot's purpose : ")

            robot = Robot(name, color, weight, purpose)
            robots[name] = robot
            print(f"\nRobot '{name}' has been added/updated")
            robot.display_info()

        #choice 2
        elif choice == "2":
            if not robots:
                print("No robot have been created yet.")
                continue
            name = input("Enter the name of the Robot you want to view: ")

            if name in robots:
                print()
                robots[name].display_info()
            else:
                print(f"\nRobot '{name}' not found. Available robots: {','.join(robots.keys())}")
        
        #choice 3
        elif choice == "3":
            if not robots:
                print("\nNo robots have been created yet. ")
                continue
            
            name = input("Enter the name of the robot you want to override: ").strip().lower()

            if name not in robots:
                print(f"\nRobot '{name}' not found. Available robots: {','.join(robots.keys())}")

            print(f"\nOverriding Robot '{name}'.... Enter new details.")

            color = input("Enter the Robot's new color: ")

            while True:
                try:
                    weight = float(input("Enter Robot's new weight: "))
                    break
                except ValueError:
                    print("Invalid Input! Enter a number for weight.")

            purpose = input("Enter Robot's new purpose: ")
            
            robot = Robot(name, color, weight, purpose)
            print(f"\nRobot '{name}' has been overriden successfully")
            robot.display_info()

        elif choice == "4":
            print("Exiting robot factory")
            break

        else:
            print("Invalid Input. Re-enter choice:")