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

    # Add node to end O(1)
    def append(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.length = 1
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    # Add node to start O(1)
    def prepend(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    # Remove node from end, then return removed value O(n)
    def pop(self):
        removed_val = None

        if self.length == 0:
            return None
        elif self.length == 1:
            removed_val = self.head.value
            self.head, self.tail, self.length = None, None, 0
        else:
            second_last_node = self.head
            for i in range(self.length - 2):
                second_last_node = second_last_node.next

            removed_val = second_last_node.next.value
            second_last_node.next = None
            self.tail = second_last_node
            self.length -= 1

        return removed_val

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
linked_list.append(10)
linked_list.print_list()
print("---------------------")
removed_val = linked_list.pop()
print("removed_val", removed_val)
linked_list.print_list()
