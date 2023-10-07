class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefixes = {0: 1}
        res = 0
        cur = 0
        for n in nums:
            cur += n
            if (cur - k) in prefixes:
                res += prefixes[cur - k]
            prefixes[cur] = prefixes.get(cur, 0) + 1
        return res
