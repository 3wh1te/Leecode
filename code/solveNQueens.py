class Solution:
    def solveNQueens(self, n: int):
        res = []
        self.fill_puzzle([None]*n,0,res)
        return res
    def fill_puzzle(self,puzzle,row,res):
        if len(puzzle) == row:
            solve = []
            for line in puzzle:
                solve_l = '.'*line + 'Q' + '.'*(row - line - 1)
                solve.append(solve_l)
            res.append(solve)
            return 0
        for col in range(len(puzzle)):
            flag = True
            for r in range(row):
                if puzzle[r] == col or abs(col - puzzle[r]) == row - r:
                    flag = False
                    break
            if flag:
                puzzle[row] = col
                self.fill_puzzle(puzzle,row + 1,res)

if __name__ == '__main__':
    print(Solution().solveNQueens(5))