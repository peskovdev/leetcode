class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(cur, used):
            if len(used) == len(nums):
                res.append(cur)
                return
            for i, n in enumerate(nums):
                if i not in used:
                    used.add(i)
                    dfs(cur + [n], used)
                    used.remove(i)

        dfs([], set())
        return res
