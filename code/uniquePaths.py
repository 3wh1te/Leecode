class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = []

        for i in range(n):
            row = []
            for j in range(m):
                if i == 0 or j == 0:
                    row.append(1)
                else:
                    row.append(row[-1] + res[-1][j])
            res.append(row)
        return res[-1][-1]

    def uniquePaths1(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
if __name__ == '__main__':
    print(Solution().uniquePaths(7, 3))
    print(Solution().uniquePaths1(7, 3))