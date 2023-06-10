class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


sol = Solution()
print(sol.runningSum([1, 2, 3, 4]))
print(sol.runningSum([1, 1, 1, 1, 1]))
print(sol.runningSum([3, 1, 2, 10, 1]))
