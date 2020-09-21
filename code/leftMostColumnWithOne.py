# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def __init__(self,matrix):
        self.matrix = matrix
    def get(self, x: int, y: int) -> int:
        return self.matrix[x][y]
    def dimensions(self):
       return [len(self.matrix), len(self.matrix[0])]

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        index = m
        # index 不断更新index位置
        for i in range(n):
            left = 0
            # 下一次从 0- index开始搜索
            right = index - 1
            # 二分搜索
            while left < right:
                mid = int((left + right) / 2)
                target = binaryMatrix.get(i, mid)
                if target == 1 and (mid == 0 or  binaryMatrix.get(i, mid - 1) == 0):
                    index = mid
                    break
                elif target == 1:
                    right = mid - 1
                elif target == 0:
                    left = mid + 1
        if index == m:
            return -1
        return index

