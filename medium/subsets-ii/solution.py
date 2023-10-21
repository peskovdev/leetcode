class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def backtrack(cur, i):
            if i == len(nums):
                res.append(cur)
                return
            backtrack(cur + [nums[i]], i + 1)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(cur, i + 1)

        backtrack([], 0)
        return res


# Or
# class Solution:
#     def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         res = set()
#
#         def dfs(cur, start):
#             res.add(tuple(cur))
#             for i in range(start, len(nums)):
#                 dfs(cur + [nums[i]], i + 1)
#
#         dfs([], 0)
#         # return res
#         return [list(el) for el in res]
