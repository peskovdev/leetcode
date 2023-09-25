class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        for i in range(len(nums) + 1):
            res = res ^ i
        return res
