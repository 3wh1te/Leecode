# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return TreeNode(preorder[0])
        if len(preorder) == 0:
            return None
        head = TreeNode(preorder[0])
        i = 0
        for i in range(len(preorder)):
            if preorder[i] > preorder[0]:
                i -= 1
                break
        i += 1
        head.left = self.bstFromPreorder(preorder[1:i])
        head.right = self.bstFromPreorder(preorder[i:])
        return head

    def bstFromPreorder1(self, preorder: List[int]) -> TreeNode:
        head = None
        pos = None
        tree_nodes = []
        i = 0
        while i < len(preorder):
            node = preorder[i]
            if pos == None:
                head = pos = TreeNode(node)
                i += 1
            else:
                if pos.val > node:
                    pos.left = TreeNode(node)
                    tree_nodes.append(pos)
                    pos = pos.left
                    i += 1
                elif pos.val < node and (len(tree_nodes) == 0 or node < tree_nodes[-1].val):
                    if pos.right == None:
                        pos.right = TreeNode(node)
                        tree_nodes.append(pos)
                        pos = pos.right
                        i += 1
                    else:
                        tree_nodes.append(pos)
                        pos = pos.right
                else:
                    pos = tree_nodes.pop()
        return head
