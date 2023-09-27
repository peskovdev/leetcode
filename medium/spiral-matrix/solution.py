class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        lp, rp = 0, len(matrix[0]) - 1
        tp, bp = 0, len(matrix) - 1

        res = []
        while lp <= rp and tp <= bp:
            # get every top i
            for i in range(lp, rp + 1):
                res.append(matrix[tp][i])
            tp += 1
            # get every right i
            for i in range(tp, bp + 1):
                res.append(matrix[i][rp])
            rp -= 1

            if not (lp <= rp and tp <= bp):
                break

            # get every bottom i
            for i in range(rp, lp - 1, -1):
                res.append(matrix[bp][i])
            bp -= 1
            # get every left i
            for i in range(bp, tp - 1, -1):
                res.append(matrix[i][lp])
            lp += 1
        return res
