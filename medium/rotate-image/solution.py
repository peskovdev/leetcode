class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """Do not return anything, modify matrix in-place instead"""
        lp, rp = 0, len(matrix) - 1

        while lp < rp:
            tp, bp = lp, rp
            for i in range(rp - lp):
                top_left = matrix[tp][lp + i]
                matrix[tp][lp + i] = matrix[bp - i][lp]
                matrix[bp - i][lp] = matrix[bp][rp - i]
                matrix[bp][rp - i] = matrix[tp + i][rp]
                matrix[tp + i][rp] = top_left
            lp, rp = lp + 1, rp - 1
