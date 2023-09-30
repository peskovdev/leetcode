class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]

        lp, rp = 0, len(matrix) - 1
        num = 1
        while lp <= rp:
            tp, bp = lp, rp

            for i in range(lp, rp + 1):
                matrix[tp][i] = num
                num += 1
            for i in range(tp + 1, bp):
                matrix[i][rp] = num
                num += 1
            for i in range(rp, lp, -1):
                matrix[bp][i] = num
                num += 1
            for i in range(bp, tp, -1):
                matrix[i][lp] = num
                num += 1
            lp, rp = lp + 1, rp - 1

        return matrix
