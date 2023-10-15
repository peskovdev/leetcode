class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        matrix = [[int(n) for n in matrix[i]] for i in range(len(matrix))]
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    matrix[row][col] += matrix[row - 1][col]
        res = 0
        for heights in matrix:
            stack: list[[int, int]] = []
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    idx, height = stack.pop()
                    res = max(res, (i - idx) * height)
                    start = idx
                stack.append((start, h))
            for i, h in stack:
                res = max(res, (len(heights) - i) * h)
        return res
