# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headB == None or headA == None:
            return None
        posA = headA
        posB = headB
        A = []
        B = []
        while posA != None:
            A.append(posA)
            posA = posA.next
        while posB != None:
            B.append(posB)
            posB = posB.next

        i = -1
        while A[i] == B[i]:
            i -= 1
            if -i > len(A):
                return A[0]
            if -i > len(B):
                return B[0]
        return A[i].next