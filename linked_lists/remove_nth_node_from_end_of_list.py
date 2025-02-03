class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None

        # Place linked list in an array
        curr_node, nodes, length = head, [], 0
        while curr_node:
            length += 1
            nodes.append(curr_node)
            curr_node = curr_node.next

        # If n targets the only existing node for removal
        if n == 1 and length == 1:
            head = None
        # If n targets the first node on a linked list with 2+ nodes
        elif n == length:
            nodes[0].next = None
            head = nodes[1]
        # If n targets the final node
        elif n == 1:
            nodes[-2].next = None
        # If n targets a node in the middle
        else:
            nodes[-n].next = None
            nodes[-n - 1].next = nodes[-n + 1]

        return head


my_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution().removeNthFromEnd(my_list, 5)

n = sol
while n:
    print(n.__dict__)
    n = n.next
