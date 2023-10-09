class Solution:
    def maxPower(self, s: str) -> int:
        res, cur = 0, 0

        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                cur = 1
            else:
                cur += 1
            res = max(res, cur)
        return res
