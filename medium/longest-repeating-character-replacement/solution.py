class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp, rp = 0, 0
        counter: dict[str, int] = {}
        maxf = 0
        res = 0
        for rp, char in enumerate(s):
            counter[char] = counter.get(char, 0) + 1
            maxf = max(maxf, counter[char])
            cur_len = rp - lp + 1
            if cur_len - maxf <= k:
                res = max(res, cur_len)
            else:
                counter[s[lp]] -= 1
                lp += 1
        return res
