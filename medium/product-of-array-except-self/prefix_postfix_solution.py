class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if nums.count(0) > 1:
            return [0 for _ in range(len(nums))]

        prefix = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            prefix[i] = nums[i] * product
            product = prefix[i]

        product = 1
        postfix = [1] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            postfix[i] = nums[i] * product
            product = postfix[i]

        for i in range(len(nums)):
            if i - 1 < 0:
                pre_product = 1
            else:
                pre_product = prefix[i - 1]

            if i + 1 >= len(nums):
                post_product = 1
            else:
                post_product = postfix[i + 1]

            nums[i] = pre_product * post_product

        return nums


sol = Solution()
res = sol.productExceptSelf([1, 2, 3, 4])
assert res == [24, 12, 8, 6], res
