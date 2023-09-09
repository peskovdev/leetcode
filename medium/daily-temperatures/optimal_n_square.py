class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures) - 1, -1, -1):
            shift = 1
            while i + shift < len(temperatures):
                if temperatures[i] < temperatures[i + shift]:
                    res[i] = shift
                    break
                if res[i + shift] == 0:
                    break
                shift += res[i + shift]

        return res
