from typing import Optional


class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def hasCycle(self, head=Optional[ListNode]):
        if head is None or head.next is None:
            return False

        n1, n2 = head, head
        while True:
            n1 = n1.next
            n2 = n2.next.next if n2.next is not None else None

            if n2 is None or n1 is None:
                return False
            if n1 == n2:
                return True

