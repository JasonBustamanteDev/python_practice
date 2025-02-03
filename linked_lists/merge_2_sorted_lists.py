# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Combine 2 sorted linked lists into 1 sorted linked list
    def mergeTwoLists(self, list1, list2):
        # Niche cases
        if list1 is None and list2 is None:
            return None
        if list1 is not None and list2 is None:
            return list1
        if list1 is None and list2 is not None:
            return list2

        cond = list1.val < list2.val
        head = list1 if cond else list2
        p1, p2 = list1, list2

        prev = head
        p1 = p1.next if cond else p1
        p2 = p2.next if cond is False else p2
        while True:
            # Both are none
            if p1 is None and p2 is None:
                break
            # One of them is none
            elif p1 is None and p2 is not None:
                prev.next = p2
                prev = p2
                p2 = p2.next
            elif p2 is None and p1 is not None:
                prev.next = p1
                prev = p1
                p1 = p1.next
            # Neither is none
            elif p2.val <= p1.val:
                prev.next = p2
                prev = p2
                p2 = p2.next
            elif p1.val < p2.val:
                prev.next = p1
                prev = p1
                p1 = p1.next

        return head


l1 = ListNode(1, ListNode(5))
l2 = ListNode(0)
sol = Solution().mergeTwoLists(l1, l2)

while sol is not None:
    print(sol.val)
    sol = sol.next
