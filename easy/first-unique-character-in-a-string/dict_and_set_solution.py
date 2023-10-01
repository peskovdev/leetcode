class Solution:
    def firstUniqChar(self, s: str) -> int:
        last_index = {}
        char_set = set()
        for i, c in enumerate(s):
            if c in char_set:
                if c in last_index:
                    del last_index[c]
            else:
                last_index[c] = i
                char_set.add(c)
        return min(last_index.values()) if last_index else -1
