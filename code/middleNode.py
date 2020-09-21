# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pos = head
        i = 1
        while pos.next != None:
            i += 1
            pos = pos.next
        res = head
        j = 0
        while j < int(i/2):
            res = res.next
            j += 1

        return res
