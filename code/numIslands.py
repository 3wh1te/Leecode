from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        row = 0
        col = 0
        # DFS
        def dfs(grid, row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            dfs(grid, row + 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row - 1, col)
            dfs(grid, row, col - 1)
        while row < len(grid):
            while row < len(grid) and grid[row][col] == '0' :
                row += int((col + 1) / len(grid[0]))
                col = (col + 1) % len(grid[0])
            if row < len(grid):
                res += 1
                dfs(grid, row, col)
        return res


if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(Solution().numIslands(grid))
