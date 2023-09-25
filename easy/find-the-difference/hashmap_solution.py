from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s, count_t = Counter(s), Counter(t)
        for c in count_t:
            if count_s[c] != count_t[c]:
                return c
