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
input_values = ["I", "S", "L", "T", "O", "R", "N", "S", "U", "D", "L", "A", "V"]
target_values = "LINUS TORVALDS"

# Create an empty linked list
linked_list = LinkedList()

# Insert the input values in such a way that they form the target name
for letter in target_values:
    linked_list.insert(letter)

# Display the linked list
linked_list.display()
