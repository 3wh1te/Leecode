class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = []
        n = len(matrix)
        for col in range(n):
            new_row = []
            for row in range(n):
                new_row.append(matrix[n - row - 1][col])
            new_matrix.append(new_row)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = new_matrix[i][j]
        print(matrix)









if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
