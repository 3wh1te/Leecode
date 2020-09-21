class Solution:
    def searchMatrix(self, matrix, target):
        def search(matrix,row,col,target):
            if row < 0 or col >= len(matrix[0]):
                return False
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                return search(matrix, row, col + 1, target)
            else:
                return search(matrix, row - 1, col, target)
        return search(matrix,len(matrix) - 1, 0, target)


    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        right_x,right_y = len(matrix),len(matrix[0])
        left_x,left_y = 0, 0
        return self.binary_search_m(matrix, left_x, left_y, right_x, right_y, target)

    def binary_search_m(self,matrix,left_x,left_y,right_x,right_y,target):
        lx,ly,rx,ry = left_x,left_y,right_x,right_y
        if right_x == left_x and right_y == left_y:
            if matrix[left_x][left_y] != target:
                return False
            else:
                return True
        mid,mid_x,mid_y = 0,0,0
        while right_x >= left_x and right_y >= left_y:
            mid_x = int((right_x + left_x - 1) / 2)
            mid_y = int((right_y + left_y - 1) / 2)
            mid = matrix[mid_x][mid_y]
            if mid == target:
                return True
            elif mid < target:
                left_x, left_y = mid_x + 1, mid_y + 1
            else:
                right_x, right_y = mid_x - 1, mid_y - 1
        # 分两部分大于mid_x,小于mid_y : larger than mid_y litte than mid_x
        # 上
        print(mid)
        top = self.binary_search_m(matrix, lx, mid_y, mid_x, ry, target)
        if top:
            return top
        # 下
        bottom = self.binary_search_m(matrix, mid_x, ly, rx, mid_y, target)

        return bottom


if __name__ == '__main__':
    # 先二分搜索对角线，再二分搜索列和行
    matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    print(Solution().searchMatrix(matrix,12))
    print(Solution().searchMatrix(matrix, 20))