class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head, self.tail, self.length = new_node, new_node, 1

    # Add node to end O(1)
    def append(self, val):
        new_node = Node(val)

        if self.length == 0:
            self.length = 1
            self.head, self.tail = new_node, new_node
        else:
            self.length += 1
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Add node to start O(1)
    def prepend(self, val):
        new_node = Node(val)

        if self.length == 0:
            self.length = 1
            self.head, self.tail = new_node, new_node
        else:
            self.length += 1
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Remove node from end, then return removed value O(1)
    def pop(self):
        if self.length == 1:
            removed_value = self.head.value
            self.length = 0
            self.head, self.tail = None, None
        else:
            removed_value = self.tail.value
            self.length -= 1

            node_before_tail = self.tail.prev
            node_before_tail.next = None
            self.tail.prev = None
            self.tail = node_before_tail

        return removed_value

    # Remove node from start and return removed value O(1)
    def pop_first(self):
        if self.length == 1:
            removed_value = self.head.value
            self.length = 0
            self.head, self.tail = None, None
        else:
            removed_value = self.head.value
            self.length -= 1

            node_after_head = self.head.next
            self.head.next = None
            node_after_head.prev = None
            self.head = node_after_head

        return removed_value

    # Add node at index i
    def insert(self, target_index, val):
        if target_index < 0 or target_index > self.length:
            return False
        elif target_index == self.length:
            self.append(val)
        elif target_index == 0:
            self.prepend(val)
        else:
            temp_node, current_index = self.head, 0
            while current_index <= target_index:
                if current_index == target_index:
                    node_before_target = temp_node.prev
                    # Technically this is the node at the target index
                    # But it will be shifted over by 1 soon (hence the name node_after_target)
                    node_after_target = temp_node  
                    break

                temp_node = temp_node.next
                current_index += 1

            new_node = Node(val)
            self.length += 1
            node_before_target.next = new_node
            new_node.prev = node_before_target
            new_node.next = node_after_target
            node_after_target.prev = new_node

        return True

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


dll = DoublyLinkedList(5)
dll.append(8)
dll.append(1)
dll.print_list()
