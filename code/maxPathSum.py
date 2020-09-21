# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = -2147483648
        def maxPath(root, max_path):
            if root == None:
                return 0, max_path
            left, lmax = maxPath(root.left, max_path)
            right, rmax = maxPath(root.right, max_path)
            max_path = max(lmax, rmax)
            max_path = max(max_path, max(left, 0) + max(right, 0) + root.val)
            return max(0, max(left, right)) + root.val, max_path
        _ ,max_path = maxPath(root,max_path)
        return max_path
