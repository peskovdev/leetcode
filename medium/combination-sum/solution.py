class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(nums, cur_sum, left_limit):
            if cur_sum == target:
                res.append(nums)
            elif cur_sum < target:
                for i in range(left_limit, len(candidates)):
                    dfs(nums + [candidates[i]], cur_sum + candidates[i], i)

        dfs([], 0, 0)
        return res


# or
# class Solution:
#     def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
#         res = []
#         def dfs(nums, cur, idx):
#             if cur == target:
#                 res.append(nums)
#             elif idx < len(candidates) and cur < target:
#                 dfs(nums + [candidates[idx]], cur + candidates[idx], idx)
#                 dfs(nums, cur, idx + 1)
#         dfs([], 0, 0)
#         return res
