class Solution:
    def trap(self, height: list[int]) -> int:
        mins, lmax, rmax = [0] * len(height), 0, 0
        for i in range(len(height)):
            mins[i] = lmax
            lmax = max(lmax, height[i])

        res = 0
        for i in range(len(height) - 1, -1, -1):
            mins[i] = min(mins[i], rmax)
            rmax = max(rmax, height[i])
            res += max(0, (mins[i] - height[i]))

        return res
