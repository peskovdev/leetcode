class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        lp = 0
        zero_index = -1
        res = 0
        for rp in range(len(nums)):
            if nums[rp] == 0:
                if zero_index != -1:
                    lp = 1 + zero_index
                zero_index = rp
            res = max(res, (rp - lp))

        return res
