class Node:
    def __init__(self, value):
        # We create a node class since several LL actions require us to create a new node (reduces code repetition)
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        starter_node = Node(value)
        self.head = starter_node
        self.tail = starter_node
        self.length = 1

    def append(self):
        # Add node to end
        pass
    def prepend(self):
        # Add node to start
        pass
    def pop(self):
        # Remove node from end
        pass
    def pop_first(self):
        # Remove node from start
        pass
    def insert(self):
        # Add node at index i
        pass
    def remove(self):
        # Remove node at index i
        pass
    def lookup_by_value(self):
        # Find node with a value equal to the input
        pass
    def lookup_by_index(self):
        # Find node at position i (keep in mind lLL's have no actual indexes)
        pass
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


linked_list = LinkedList(4)
linked_list.print_list()