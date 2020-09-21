#coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        l3 = ListNode(-1)
        carried = 0


        while l1 != None and l2 != None:
            a = l1.val
            b = l2.val
            sum = a + b + carried
            carried = int(sum/10)
            l = ListNode(sum - carried *10)
            if l3.val == -1:
                l3 = l
                head = l3
            else:
                l3.next = l
                l3 = l3.next


            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            a = l1.val
            b = 0
            sum = a + b + carried
            carried = int(sum/10)
            l = ListNode(sum - carried *10)
            if l3.val == -1:
                l3 = l
                head = l3
            else:
                l3.next = l
                l3 = l3.next

                l1 = l1.next

        while l2 != None:
            b = l2.val
            a = 0
            sum = a + b + carried
            carried = int(sum/10)
            l = ListNode(sum - carried *10)
            if l3.val == -1:
                l3 = l
                head = l3
            else:
                l3.next = l
                l3 = l3.next

                l2 = l2.next

        return head


if __name__ == "__main__":
    Node1 = ListNode(2)
    Node2 = ListNode(4)
    Node3 = ListNode(3)
    Node4 = ListNode(5)
    Node5 = ListNode(6)
    Node6 = ListNode(4)

    Node1.next = Node2
    Node2.next = Node3
    Node4.next = Node5
    Node5.next = Node6

    s = Solution
    n = s.addTwoNumbers(s, Node1, Node4)

    while n is not None:
        print(n.val)
        n = n.next
