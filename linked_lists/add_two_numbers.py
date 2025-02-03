class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        n1, n2 = l1, l2
        carry_over = 0
        temp_head = ListNode(-99)
        curr_node = temp_head

        while n1 is not None or n2 is not None:
            n1_val = n1.val if n1 is not None else 0
            n2_val = n2.val if n2 is not None else 0

            sum = n1_val + n2_val + carry_over
            if sum < 10:
                carry_over = 0
                curr_node.next = ListNode(sum)
            else:
                carry_over = 1
                curr_node.next = ListNode(sum-10)

            curr_node = curr_node.next

            n1 = n1.next if n1 is not None else None
            n2 = n2.next if n2 is not None else None
            
        # Perform final carryover if last sum ended up being above 10
        if carry_over == 1:
            curr_node.next = ListNode(1)
            curr_node = curr_node.next
        
        return temp_head.next


l1 = ListNode(9, ListNode(9))
l2 = ListNode(1, ListNode(1))
sol = Solution().addTwoNumbers(l1, l2)
n = sol
while n:
    print(n.__dict__)
    n = n.next