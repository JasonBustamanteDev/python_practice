class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head, self.tail, self.length = new_node, new_node, 1

    # Add node to end
    def append(self, val):
        pass

    # Add node to start
    def prepend(self, val):
        pass

    # Remove node from end, then return removed value
    def pop(self):
        pass

    # Remove node from start and return removed value
    def pop_first(self):
        pass

    # Add node at index i
    def insert(self, target_index, val):
        pass

    # Remove node at index i, then return the removed value
    def remove(self, target_index):
        pass

    # Return node with a value equal to the input
    def lookup_by_value(self, target_val):
        pass

    # Return node at position i
    def lookup_by_index(self, target_index):
        pass

    def print_list(self):
        list = []
        temp = self.head
        while temp is not None:
            list.append(temp.value)
            temp = temp.next
        print(f"Length {self.length} → {list}")
