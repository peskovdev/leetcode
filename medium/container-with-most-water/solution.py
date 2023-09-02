class Solution:
    def maxArea(self, height: list[int]) -> int:
        lp, rp = 0, len(height) - 1

        max_square = 0
        while lp < rp:
            square = (rp - lp) * min(height[lp], height[rp])
            if square > max_square:
                max_square = square

            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1

        return max_square
