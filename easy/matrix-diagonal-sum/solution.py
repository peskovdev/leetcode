class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res, n = 0, len(mat) - 1
        for i in range(len(mat)):
            res += mat[i][i]
            if i != (n - i):
                res += mat[n - i][i]

        return res


# Or with substraction
# class Solution:
#     def diagonalSum(self, mat: list[list[int]]) -> int:
#         res, n = 0, len(mat)
#         for i in range(len(mat)):
#             res += mat[i][i]
#             res += mat[n - 1 - i][i]
#
#         return res - (mat[n // 2][n // 2] if n % 2 else 0)
