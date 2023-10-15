class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        for i in range(len(matrix)):
            matrix[i].append(0)
        matrix.append([0 for i in range(len(matrix[0]))])

        res = 0
        for row in range(len(matrix) - 2, -1, -1):
            for col in range(len(matrix[0]) - 2, -1, -1):
                if matrix[row][col] == "1":
                    bot = matrix[row + 1][col]
                    diag = matrix[row + 1][col + 1]
                    right = matrix[row][col + 1]
                    matrix[row][col] = 1 + min(bot, diag, right)
                    res = max(res, matrix[row][col])
                else:
                    matrix[row][col] = 0

        return res**2
