class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        curr_node, prev_node = head, None

        while curr_node is not None:
            old_next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = old_next

        return prev_node