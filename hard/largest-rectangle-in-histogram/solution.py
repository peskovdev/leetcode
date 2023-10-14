class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack: list[[int, int]] = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, (i - idx) * height)
                start = idx
            stack.append((start, h))

        for idx, height in stack:
            res = max(res, (len(heights) - idx) * height)
        return res
