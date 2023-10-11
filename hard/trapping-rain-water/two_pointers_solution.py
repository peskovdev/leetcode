class Solution:
    def trap(self, height: list[int]) -> int:
        lp, rp = 0, len(height) - 1
        lmax, rmax = height[0], height[-1]

        res = 0
        while lp < rp:
            if lmax < rmax:
                res += max(0, lmax - height[lp])
                lp += 1
                lmax = max(lmax, height[lp])
            else:
                res += max(0, rmax - height[rp])
                rp -= 1
                rmax = max(rmax, height[rp])
        return res
