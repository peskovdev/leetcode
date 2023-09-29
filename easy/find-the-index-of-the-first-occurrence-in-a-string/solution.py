class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lp = 0
        for rp in range(len(needle), len(haystack) + 1):
            if haystack[lp:rp] == needle:
                return lp
            lp += 1
        return -1
