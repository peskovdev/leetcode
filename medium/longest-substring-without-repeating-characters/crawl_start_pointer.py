class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashchar: set[str] = set()

        start = 0
        res = 0
        for cur, c in enumerate(s):
            while c in hashchar:
                hashchar.remove(s[start])
                start += 1
            hashchar.add(c)
            res = max(res, cur - start + 1)
        return res
