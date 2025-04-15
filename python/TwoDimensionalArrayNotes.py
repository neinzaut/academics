'''
	Two-dimensional/multi-dimensional array
	- an array with two or more indexes[subscript]
		-- as i (row) and j (column)

	Syntax: arrayName[index1][index2]

	Create a 2x3

	fruits = | banana | apple | orange |
			 | cherry | kiwi  | peach  |

	fruits[0][1] = apple

'''

# Create a 2 x 3
fruits = [
    ["banana", "apple", "cherry"],
    ["cherry", "kiwi", "peach"]
    ]
print(fruits)
print(fruits[0])
print(fruits[1])

'''
java version:
for(i = 0; i < row; i++)
    for(j = 0; j < columns; j++)
'''
#python version:
for row in fruits:
    for fruit in row:
        print(f"| {fruit} ", end = "")
    print("|")



# Accessing elements:
#arrayName[index1][index2] = element/item
print(fruits[1][2]) #peach
#print(fruits[1][3]) #index out of reach

# Modifying values:
fruits[0][1] = "mango"
print(fruits)

# Iterating rows and columns:
for row in fruits:
    print(row)

# Iterating in columns
array2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

num_rows = len(array2D)
num_cols = len(array2D[0])
for col in range(num_cols):
    column_values = [array2D[row][col] for row in range (num_rows)] #pa-vertical ang pagread ng column
    print(f"Columns {col}: {column_values}")

    # Calculate the following (in columns): total_sum, total_elements, average
    total_sum_col = sum(column_values)
    print("Total Sum (Column): ", total_sum_col)

    total_elements = len(column_values)
    print("Total Elements: ", total_elements)

    average = total_sum_col / total_elements
    print("Average: ", average)

total_sum = sum(sum(row) for row in array2D)
print("\nTotal Sum (Row): ", total_sum)

max_value = max(max(row) for row in array2D)
print("Max Value: ", max_value)

