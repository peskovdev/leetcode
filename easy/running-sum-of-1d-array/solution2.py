class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        for i, element in enumerate(nums):
            sum += element
            nums[i] = sum
        return nums


sol = Solution()
print(sol.runningSum([1, 2, 3, 4]))
print(sol.runningSum([1, 1, 1, 1, 1]))
print(sol.runningSum([3, 1, 2, 10, 1]))
