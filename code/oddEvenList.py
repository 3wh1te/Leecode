# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next == None:
            return head
        e = head.next
        odd = head
        even = head.next
        pos = even.next
        i = 3
        while pos != None:
            if i % 2 == 0:
                even.next = pos
                even = even.next
                pos = pos.next
            else:
                odd.next = pos
                odd = odd.next
                pos = pos.next
            i += 1
        even.next = None
        odd.next = e
        return head
if __name__ == '__main__':
    print(Solution().oddEvenList(ListNode(3)))
    print(Solution().oddEvenList(ListNode(3)))