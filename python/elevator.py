# AGGABAO, LUMAKANG, TUAZON

import time

#Ascii Art separated kasi ayaw niya mag-display nung current floor ng maayos >:( 
ELEVATOR_ASCII = """
█████████████████████████████████████████
█████████████        {}        ███████████
█████████████████████████████████████████
█░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░█
█████████████████████████████████████████
█████████████████████████████████████████
"""

OPEN_ELEVATOR_ASCII = """
█████████████████████████████████████████
█████████████        {}        ███████████
█████████████████████████████████████████
█░░░░░|                            |░░░░█
█░░░░░|                            |░░░░█
█░░░░░|                            |░░░░█
█░░░░░|                            |░░░░█
█░░░░░|                            |░░░░█
█░░░░░|                            |░░░░█
█░░░░░|                            |░░░░█
█░░░░░|                            |░░░░█
█████████████████████████████████████████
█████████████████████████████████████████
"""

def display_elevator(current_floor):
    return ELEVATOR_ASCII.format(current_floor)

def display_elevator_open(target_floor):
    return OPEN_ELEVATOR_ASCII.format(target_floor)

def elevator(total_floors):
    current_floor = 1
    print("Current Floor:", current_floor)


    #i tried to make a panel of buttons pero di na kinaya ng brain ko @@
    #try niyo lagyan yung sa array thingy para magprint siya ng column chuchu
    while True:
        print("\nOptions:")
        print("1. Go up")
        print("2. Go down")
        print("3. Go to another floor")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            target_floor = current_floor + 1
            if target_floor <= total_floors:
                for floor in range(current_floor, target_floor + 1):
                    print(display_elevator(floor))
                    time.sleep(1)
                current_floor = target_floor
                print(display_elevator_open(floor))
                print("You have reached Floor", current_floor)
            else:
                print("Already at the top floor.")

        elif choice == "2":
            target_floor = current_floor - 1
            if target_floor >= 1:
                for floor in range(current_floor, target_floor - 1, -1):
                    print(display_elevator(floor))
                    time.sleep(1)
                current_floor = target_floor
                print(display_elevator_open(floor))
                print("You have reached Floor", current_floor)
            else:
                print("Already at the ground floor.")

        elif choice == "3":
            target_floor = int(input("Enter the target floor: "))
            if 1 <= target_floor <= total_floors:
                direction = "up" if target_floor > current_floor else "down"
                for floor in range(current_floor, target_floor + 1) if direction == "up" else range(current_floor, target_floor - 1, -1):
                    print(display_elevator(floor))
                    time.sleep(1)
                current_floor = target_floor
                print(display_elevator_open(floor))
                print("You have reached Floor", current_floor)
            else:
                print("Invalid floor number. Please enter a valid floor number.")

        elif choice == "4":
            print("Exiting the elevator.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

total_floors = int(input("Enter the total number of floors: "))
elevator(total_floors)