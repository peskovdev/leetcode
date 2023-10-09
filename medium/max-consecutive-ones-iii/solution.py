class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        lp = 0
        zeros = 0
        res = 0
        for rp in range(len(nums)):
            if nums[rp] == 0:
                zeros += 1
                while zeros > k:
                    if nums[lp] == 0:
                        zeros -= 1
                    lp += 1
            res = max(res, (rp - lp + 1))

        return res
