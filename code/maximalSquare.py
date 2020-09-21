from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area = 0
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    matrix[i][j] = 1
                    area = 1
                    max_area = 1
                else:
                    matrix[i][j] = 0
        if area == 0:
            return 0
        flag = True
        while flag:
            flag = False
            for i in range(len(matrix)-1):
                for j in range(len(matrix[0])-1):
                    if matrix[i][j] == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1] == area:
                        max_area = area + 1
                        matrix[i][j] = max_area
                        flag = True
            area = max_area
        res = area**2
        return res
if __name__ == '__main__':
    # print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    # print(Solution().maximalSquare([['0', '0'],['0', '0']]))
    a = [9]
    print(a[1:1])

