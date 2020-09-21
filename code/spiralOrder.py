class Solution:
    def spiralOrder(self, matrix):
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        res = []
        direction = 0
        while left <= right and top <= bottom:
            if direction%4 == 0:
                # top
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
            elif direction%4 == 1:
                # right
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1
            elif direction % 4 == 2:
                # bottom
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            else:
                # left
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            direction += 1

        return res











if __name__ == '__main__':
    matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
    Solution().spiralOrder(matrix)