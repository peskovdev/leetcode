class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = 0
        max_sum = 0
        for el in nums:
            if current_sum + el <= 0:
                current_sum = 0
            else:
                current_sum += el
                if max_sum < current_sum:
                    max_sum = current_sum
        if max_sum <= 0:
            return max(nums)
        return max_sum


sol = Solution()

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
assert sol.maxSubArray(nums) == 6
nums = [1]
assert sol.maxSubArray(nums) == 1
nums = [5, 4, -1, 7, 8]
assert sol.maxSubArray(nums) == 23
