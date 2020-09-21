# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def diameter(root: TreeNode):
            if root == None:
                return 0,0
            l_deepth, l_diameter = diameter(root.left)
            r_deepth, r_diameter = diameter(root.right)
            return max(l_deepth,r_deepth) + 1, max(r_diameter,l_diameter,l_deepth + r_deepth)
        deepth, res = diameter(root)
        # 最大深度+2
        return res
