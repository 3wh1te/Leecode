from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def minPath(grid, x, y):
            up_path = 0
            left_path = 0
            if x > 0 and y > 0:
                up_path = minPath(grid, x - 1, y)
                left_path = minPath(grid, x, y - 1)
                return min(up_path, left_path) + grid[x][y]
            if x > 0:
                return minPath(grid, x - 1, y) + grid[x][y]
            if y > 0:
                return minPath(grid, x, y - 1) + grid[x][y]
            return min(up_path, left_path) + grid[x][y]
        return minPath(grid,len(grid) - 1, len(grid[0]) - 1)

    def minPathSum1(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i > 0:
                    grid[i][j] += grid[i-1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]

if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(grid))
    print(Solution().minPathSum1(grid))



