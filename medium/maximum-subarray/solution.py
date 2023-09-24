class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        cur = 0
        for val in nums:
            cur += val
            res = max(res, cur)
            if cur < 0:
                cur = 0
        return res


sol = Solution()

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
assert sol.maxSubArray(nums) == 6
nums = [1]
assert sol.maxSubArray(nums) == 1
nums = [5, 4, -1, 7, 8]
assert sol.maxSubArray(nums) == 23
