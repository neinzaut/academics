"""
Write an algorithm, pseudocode, and code in Python to find the maximum element in a two-dimensional array. The array should 3 x 3 and student can provide their own given.

Instructions:
You are given a two-dimensional array, array, containing integer elements.

1. Write an algorithm to find the maximum element in the array.
2. Implement the algorithm in pseudocode.
3. Translate the pseudocode into Python code.
4. Test your code with the provided array.
5. Print the maximum element found in the array.
6. Ensure that your code is efficient and handles all possible edge cases.
"""

"""
ALGORITHM:
1. Create empty array for elements (elements)
2. Create an empty list for each row's data (user_input)
3. While counter is less than or equal to 3, ask for 3 number inputs.
    4. Append input to user_input list
    5. Update counter value
    6. Append user_input to grade_composition
7. Display array for double-checking. 
8. Get the maximum value of row 1, row 2, and row 3, respectively.
9. Compare each row's maximum value and get the maximum of the three values. 
10. Print the maximum value.

"""

"""
PSEUDOCODE:
Start
Create 'elements' array
Initialize counter = 1
While counter <= 3
    Create 'user_input' array
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    Append the number inputs to 'user_input' array.
    Increment the counter value
    Append 'user_input' to 'elements'
Display the array.

For row in elements
    Create 'max_values' array
    for row in elements:
        maximum_val = row[0]
        for num in row:
            if num > maximum_val:
                maximum_val = num
        Append values to 'max_values' array

    for val in max_values:
        maximum = max_values[0]
        for current in max_values:
            if current > maximum:
                maximum = current
    Print maximum



"""


elements = [ ] #2d array; will store 3 rows of user_input

def input_elements():
    current_row = 1
    counter = 1

    while counter <= 3:
        user_input = []
        print(f"\nROW {current_row}")
        num1 = int(input("Enter the first number: "))
        user_input.append(num1)
        num2 = int(input("Enter the second number: "))
        user_input.append(num2)
        num3 = int(input("Enter the third number: "))
        user_input.append(num3)

        counter = counter + 1
        current_row = current_row + 1
        elements.append(user_input)

def display_array():
    print(f"\nCOMPILED ARRAY INPUTS: {elements}\n")

def get_max():
    max_values = []
    for row in elements:
        maximum_val = row[0]  # Set the initial maximum value for each row
        for num in row:
            if num > maximum_val:
                maximum_val = num
        max_values.append(maximum_val)

    for val in max_values:
        maximum = max_values[0]
        for current in max_values:
            if current > maximum:
                maximum = current
    print("Maximum: ", maximum)

def Main():
    input_elements()
    display_array()
    get_max()
            
Main()