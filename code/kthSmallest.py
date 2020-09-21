# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = [root]
        res = root.val
        while k != 0:
            if stack[-1].left != None:
                stack.append(stack[-1].left)
                stack[-2].left = None
            elif stack[-1].right != None:
                k -= 1
                stack.append(stack[-1].right)
                res = stack.pop(-2).val
            else:
                k -= 1
                res = stack.pop(-1).val
        return res



