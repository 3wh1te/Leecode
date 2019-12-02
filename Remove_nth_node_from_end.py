#coding=utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []

        while (head.next != None):
            l.append(head)
            head = head.next
        length = len(l)
        if n == 1:
            l[-1] = None
        elif n == length:
            return l[1]
        else:
            l[-n - 1].next = l[-n + 1]
        return l[0]

if __name__ == '__main__':
    print(Solution().removeNthFromEnd())