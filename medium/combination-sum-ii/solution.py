class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(start, nums, cur_sum):
            if cur_sum == target:
                res.append(nums.copy())
            elif cur_sum < target:
                prev = -1
                for i in range(start, len(candidates)):
                    if candidates[i] != prev:
                        nums.append(candidates[i])
                        backtrack(i + 1, nums, cur_sum + candidates[i])
                        prev = nums.pop()

        backtrack(0, [], 0)
        return res


# Or
# class Solution:
#     def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
#         candidates.sort()
#         res = []
#
#         def backtrack(i, nums, cur_sum):
#             if cur_sum == target:
#                 res.append(nums.copy())
#             elif i < len(candidates) and cur_sum < target:
#                 # include num
#                 nums.append(candidates[i])
#                 backtrack(i + 1, nums, cur_sum + candidates[i])
#
#                 # not include
#                 nums.pop()
#                 while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
#                     i += 1
#                 backtrack(i + 1, nums, cur_sum)
#
#         backtrack(0, [], 0)
#         return res
