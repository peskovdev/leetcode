class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def fill(subset: list[int], index: int) -> None:
            res.append(subset)
            for i in range(index, len(nums)):
                fill(subset + [nums[i]], i + 1)

        fill([], 0)
        return res


# or
# class Solution:
#     def subsets(self, nums: list[int]) -> list[list[int]]:
#         res = []
#
#         def dfs(subset: list[int], i: int) -> None:
#             if i == len(nums):
#                 res.append(subset)
#             else:
#                 dfs(subset, i + 1)
#                 dfs(subset + [nums[i]], i + 1)
#
#         dfs([], 0)
#         return res
