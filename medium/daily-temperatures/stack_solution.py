class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack: list[list] = []  # pair: [index, temperature]

        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][1]:
                prev, _ = stack.pop()
                res[prev] = i - prev
            stack.append([i, tmp])
        return res
