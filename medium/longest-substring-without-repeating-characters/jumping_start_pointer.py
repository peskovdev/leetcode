class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter: dict[str, int] = {}
        hashindex: dict[str, int] = {}

        start, cur = 0, 0
        res = 0
        while cur < len(s):
            c = s[cur]
            if hashindex.get(c) is not None and hashindex[c] < start:
                hashindex.pop(c)
                counter.pop(c)
            counter[c] = counter.get(c, 0) + 1
            if counter[c] < 2:
                res = max(res, cur - start + 1)
            else:
                start = hashindex[c] + 1
                counter[c] -= 1
            hashindex[c] = cur
            cur += 1
        return res
