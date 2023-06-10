class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        res_array = []
        for element in nums:
            sum += element
            res_array.append(sum)
        return res_array


sol = Solution()
print(sol.runningSum([1, 2, 3, 4]))
print(sol.runningSum([1, 1, 1, 1, 1]))
print(sol.runningSum([3, 1, 2, 10, 1]))
