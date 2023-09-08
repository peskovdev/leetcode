class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            row = []
            tmp = [0] + res[-1] + [0]
            for j in range(len(res[-1]) + 1):
                row.append(tmp[j] + tmp[j + 1])
            res.append(row)
        return res
