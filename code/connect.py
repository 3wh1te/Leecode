
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        root.left = self.connect(root.left)
        root.right = self.connect(root.right)
        # connect
        lpos = root.left
        rpos = root.right
        while lpos != None:
            lpos.next = rpos
            lpos = lpos.right
            rpos = rpos.left
        return root
