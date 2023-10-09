class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        lp, rp = 0, len(nums) - 1
        res = []
        while lp <= rp:
            if abs(nums[lp]) > abs(nums[rp]):
                res.append(nums[lp] ** 2)
                lp += 1
            else:
                res.append(nums[rp] ** 2)
                rp -= 1

        return res[::-1]
