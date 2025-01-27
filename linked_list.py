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

    def append(self, val):
        # GOAL: Add node to end
        new_node = Node(val)
        if self.length == 0:
            self.length = 1
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, val):
        # GOAL: Add node to start
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def pop(self):
        # GOAL: Remove node from end
        # If list only has 1 node left
        # If list has more than 1 node left
        pass

    def pop_first(self):
        # GOAL: Remove node from start
        # If list only has 1 node left
        # If list has more than 1 node left
        pass

    def insert(self):
        # GOAL: Add node at index i
        # If list is empty
        # If list has 1 node or more
        pass

    def remove(self):
        # GOAL: Remove node at index i
        # If list has 1 node left
        # If list has more than 1 node left
        pass

    def lookup_by_value(self):
        # GOAL: Find node with a value equal to the input
        pass

    def lookup_by_index(self):
        # GOAL: Find node at position i (keep in mind lLL's have no actual indexes)
        pass

    def print_list(self):
        print("Length of LL is ", self.length)
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


linked_list = LinkedList(4)
linked_list.prepend(7)
# linked_list.append(7)
linked_list.print_list()
