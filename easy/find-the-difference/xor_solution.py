class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for c in t:
            res = res ^ ord(c)
        for c in s:
            res = res ^ ord(c)
        return chr(res)
