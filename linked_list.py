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
            for _ in range(self.length - 2):
                second_last_node = second_last_node.next

            removed_val = second_last_node.next.value
            second_last_node.next = None
            self.tail = second_last_node
            self.length -= 1

        return removed_val

    # Remove node from start and return removed value O(1)
    def pop_first(self):
        removed_val = None

        if self.length == 0:
            return None
        elif self.length == 1:
            removed_val = self.head.value
            self.head, self.tail, self.length = None, None, 0
        else:
            original_head = self.head
            self.head = self.head.next
            original_head.next = None
            self.length -= 1
            removed_val = original_head.value

        return removed_val

    # Add node at index i
    def insert(self):
        # If list is empty
        # If list has 1 node or more
        pass

    def remove(self):
        # GOAL: Remove node at index i
        # If list has 1 node left
        # If list has more than 1 node left
        pass

    # Return node with a value equal to the input
    def lookup_by_value(self, target_val):
        current_node = self.head

        while current_node is not None:
            if current_node.value == target_val:
                return current_node
            current_node = current_node.next

        return None

    # Return node at position i
    def lookup_by_index(self, target_index):
        curr_index, curr_node = 0, self.head

        while curr_node is not None:
            if curr_index == target_index:
                return curr_node

            curr_index += 1
            curr_node = curr_node.next

        return None

    def print_list(self):
        list = []
        temp = self.head
        while temp is not None:
            list.append(temp.value)
            temp = temp.next
        print(f"Length {self.length} → {list}")


linked_list = LinkedList(6)
linked_list.append(5)
linked_list.append(11)
linked_list.append(-7)
n = linked_list.lookup_by_value(20)
print(n)
