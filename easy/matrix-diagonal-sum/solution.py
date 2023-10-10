class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res, n = 0, len(mat) - 1
        for i in range(len(mat)):
            res += mat[i][i]
            if i != (n - i):
                res += mat[n - i][i]

        return res
