class Node:
    # initialization
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
            print(current.data, end="-> ") 
            current = current.next 
        print("None")


input_values = ["I", "S", "L", "T", "O", "R", "N", "S", "U", "D", "L", "A", "V"]
target_values = "LINUS TORVALDS"
target = []
text = ""

for letter in target_values:
    target.append(letter)

# create a linked list and compare the two values
for input_values in target:
    #for value in target:
    text = text + str(input_values)

print(text)

#target_values.display()