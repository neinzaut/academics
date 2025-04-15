'''
linked list
    - data structure for storing collection of items

    class Box{
        int data
        Box next
    }

    - has two attributes or fields in this class
        - data/item
        - box

    head.data
        - the data - the head is the first box that contains the items

    box.next
        - reflects to the next list and connected to a particular box
'''

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

# input values
input_values = [6, 3, 4, 2, 1]

# create a linked list and insert the input values
my_linked_list = LinkedList()
for value in input_values: # for every value in array, input/insert to newly created linked list
    my_linked_list.insert(value)

# display the linked list
my_linked_list.display()

'''
    Mini-Activity
    Create a new file name, name it linklist_activity_py inside the discussion folder

    Create a python program that will simulate the linked list to form a name using these input values
        input_values = ["I", "S", "L", "T", "O", "R", "N", "S", "U", "D", "L", "A", "V"]

        target_values = "LINUS TORVALDS"
'''