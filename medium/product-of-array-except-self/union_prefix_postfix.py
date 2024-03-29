class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if nums.count(0) > 1:
            return [0 for _ in range(len(nums))]

        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


sol = Solution()
res = sol.productExceptSelf([1, 2, 3, 4])
assert res == [24, 12, 8, 6], res
