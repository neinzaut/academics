class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Input values
input_values = ["I", "S", "L", "T", "O", "R", "N", "S", "U", "D", "L", "A", "V"]
target_values = "LINUS TORVALDS"

# Create a linked list and append input values
linked_list = LinkedList()
for value in input_values:
    linked_list.append(value)

# Display the linked list
linked_list.display()

# Check if the linked list forms the target name
def forms_target_name(linked_list, target_values):
    current = linked_list.head
    for char in target_values:
        if current is None or current.data != char:
            return False
        current = current.next
    return current is None

if forms_target_name(linked_list, target_values):
    print("The linked list forms the target name:", target_values)
else:
    print("The linked list does not form the target name:", target_values)
