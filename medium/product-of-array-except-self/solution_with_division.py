class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if nums.count(0) > 1:
            return [0 for _ in range(len(nums))]

        product = 1
        product_without_zero = 1
        for n in nums:
            product *= n
            if n != 0:
                product_without_zero *= n

        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(product_without_zero)
            else:
                res.append(product // nums[i])
        return res


sol = Solution()
res = sol.productExceptSelf([1, 2, 3, 4])
assert res == [24, 12, 8, 6], res
