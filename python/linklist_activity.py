'''
    Mini-Activity
    Create a new file name, name it linklist_activity_py inside the discussion folder

    Create a python program that will simulate the linked list to form a name using these input values
        input_values = ["I", "S", "L", "T", "O", "R", "N", "S", "U", "D", "L", "A", "V"]

        target_values = "LINUS TORVALDS"
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head 
        while current: 
            print(current.data, end="") 
            current = current.next 

# Define the input values and target name
input_values = ["I", "S", "L", "T", "O", "R", "N", "S", "U", "D", "L", "A", "V", " "]
target_values = "LINUS TORVALDS"
target = []
for x in target_values:
    target.append(x)

# Create linked list
my_linked_list = LinkedList()

# Compare the current letter in target and check if it is in input_values
    # If found, it is inserted into the newly-created linked list
for letter in target:
    if letter in input_values:
        my_linked_list.insert(letter)

# Display the linked list
my_linked_list.display()
