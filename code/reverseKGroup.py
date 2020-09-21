# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head:ListNode, k):
        res = []
        if head == None:
            return None
        while head is not None:
            k_nodes = [head]
            i = 1
            while i < k and head.next is not None:
                k_nodes.append(head.next)
                head = head.next
                i = i + 1

            if i == k:
                head = head.next
                for i, node in enumerate(k_nodes):
                    if i == 0:
                        node.next = None
                    else:
                        node.next = k_nodes[i - 1]
                if res == []:
                    res.append(k_nodes[-1])
                    res.append(k_nodes[0])
                else:
                    res[-1].next = k_nodes[-1]
                    res.append(k_nodes[0])
            else:
                if res == []:
                    res.append(k_nodes[0])
                else:
                    res[-1].next = k_nodes[0]
                head = None

        return res[0]
