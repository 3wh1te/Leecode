from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder.__len__() == 0 or inorder.__len__() == 0:
            return None
        root = preorder[0]
        pos = inorder.index(root)
        left = self.buildTree(preorder[1 : 1 + pos], inorder[0 : pos])
        right = self.buildTree(preorder[pos:], inorder[pos + 1:])
        return TreeNode(root, left ,right)