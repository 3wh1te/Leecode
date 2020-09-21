from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root == None and arr.__len__() == 0:
            return True
        elif root == None or arr.__len__() == 0:
            return False
        elif root.val != arr[0]:
            return False
        else:
            if (root.left != None and root.right != None) or (root.left == None and root.right == None):
                return self.isValidSequence(root.left, arr[1:]) or self.isValidSequence(root.right, arr[1:])
            elif root.left != None:
                return self.isValidSequence(root.left, arr[1:])
            elif root.right != None:
                return self.isValidSequence(root.right, arr[1:])

