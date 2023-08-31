class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                perhaps_target = num + nums[j]
                if perhaps_target == target:
                    return [i, j]
