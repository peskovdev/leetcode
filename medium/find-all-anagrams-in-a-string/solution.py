from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        count_s, count_p = {}, Counter(p)

        res = []
        lp, rp = 0, 0
        for rp in range(len(s)):
            count_s[s[rp]] = count_s.get(s[rp], 0) + 1
            if count_s == count_p:
                res.append(lp)

            if (rp - lp + 1) == len(p):
                count_s[s[lp]] -= 1
                if count_s[s[lp]] == 0:
                    del count_s[s[lp]]
                lp += 1
        return res
