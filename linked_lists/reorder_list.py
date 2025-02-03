class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        if head is None or head.next is None or head.next.next is None:
            return

        curr_node, nodes = head, []
        while curr_node:
            nodes.append(curr_node)
            curr_node = curr_node.next

        list_length = len(nodes)
        p1, p2 = 0, list_length - 1

        # In linked lists with an odd number of nodes, p1 and p2 will meet on the same node eventually
        if list_length % 2 == 1:
            while True:
                future_p1, future_p2 = p1 + 1, p2 - 1

                nodes[p1].next = nodes[p2]
                nodes[p2].next = nodes[future_p1]

                if future_p1 == future_p2:
                    nodes[future_p1].next = None
                    break
                else:
                    p1 = future_p1
                    p2 = future_p2

        # In linked lists with even number of nodes...
        # p1 and p2 will cross each other on the iteration after they're besides one another
        else:
            while True:
                nodes[p1].next = nodes[p2]
                if p1 == p2 - 1:
                    nodes[p2].next = None
                    break
                else:
                    nodes[p2].next = nodes[p1 + 1]
                    p1 += 1
                    p2 -= 1


