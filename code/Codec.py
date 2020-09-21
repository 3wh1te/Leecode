# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root != None:
            sum_n = 0
        else:
            sum_n = 1
        stack = [root]
        res = ''
        while stack.__len__() != 0 and stack.__len__() != sum_n:
            node = stack.pop(0)
            if node == None:
                sum_n += 1
                res += 'None/'
                stack.append(None)
                stack.append(None)
            else:
                if node.left == None:
                    sum_n += 1
                if node.right == None:
                    sum_n += 1
                res += str(node.val) + '/'
                stack.append(node.left)
                stack.append(node.right)
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split('/')[:-1]
        if nodes.__len__() == 0:
            return None
        root = TreeNode(int(nodes.pop(0)))
        stack = [root]
        while nodes.__len__() != 0:
            left_node = None
            right_node = None
            right = 'None'
            left = nodes.pop(0)
            if nodes.__len__() != 0:
                right = nodes.pop(0)
            if left != 'None':
                left_node = TreeNode(int(left))
            if right != 'None':
                right_node = TreeNode(int(right))
            node = stack.pop(0)
            if node != None:
                node.left = left_node
                node.right = right_node
            stack.append(left_node)
            stack.append(right_node)
        return root
if __name__ == '__main__':
    res = '1/2/3/None/None/4/5/'
    root = Codec().deserialize(res)
    print(Codec().serialize(root))
    root = Codec().deserialize('')
    print(Codec().serialize(root))
    print(root)
    root = Codec().deserialize('1/2/')
    print(Codec().serialize(root))