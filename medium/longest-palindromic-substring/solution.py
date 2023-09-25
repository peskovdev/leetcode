class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            lp, rp = i, i  # odd
            while lp >= 0 and rp < len(s) and s[lp] == s[rp]:
                if (rp - lp) + 1 > len(res):
                    res = s[lp: rp + 1]
                lp, rp = lp - 1, rp + 1

            lp, rp = i, i + 1  # even
            while lp >= 0 and rp < len(s) and s[lp] == s[rp]:
                if (rp - lp) + 1 > len(res):
                    res = s[lp: rp + 1]
                lp, rp = lp - 1, rp + 1

        return res
