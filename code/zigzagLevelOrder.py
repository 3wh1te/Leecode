from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            stack = []
        else:
            stack = [root]
        res = []
        i = 0
        while stack.__len__() != 0:
            new_stack = []
            row = []

            for node in stack:
                row.append(node.val)
                if node.left != None:
                    new_stack.append(node.left)
                if node.right != None:
                    new_stack.append(node.right)
            stack = new_stack
            if i % 2 == 1:
                row.reverse()
            res.append(row)
            i += 1
        return res
    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root == None:
            return res
        left = self.zigzagLevelOrder(root.left)
        right = self.zigzagLevelOrder(root.right)
        res.append([root.val])
        for i in range(min(len(right), len(left))):
            res.append(right[i] + left[i])
            if i != 0:
                res[i + 1].reverse()

        if len(right) > len(left):
            for i in range(len(left), len(right)):
                res.append(right[i])
        else:
            for i in range(len(right), len(left)):
                res.append(left[i])

        for level in res:
            level.reverse()
        return res