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

    def append():
        # Add node to end
        pass
    def prepend():
        # Add node to start
        pass
    def pop():
        # Remove node from end
        pass
    def pop_first():
        # Remove node from start
        pass
    def insert():
        # Add node at index i
        pass
    def remove():
        # Remove node at index i
        pass
    def lookup_by_value():
        # Find node with a value equal to the input
        pass
    def lookup_by_index():
        # Find node at position i (keep in mind lLL's have no actual indexes)
        pass

linked_list = LinkedList(4)
print(linked_list)