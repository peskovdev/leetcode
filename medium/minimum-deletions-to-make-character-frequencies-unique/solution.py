from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)

        res = 0
        slots = set()
        for freq in counter.values():
            while freq > 0 and freq in slots:
                res += 1
                freq -= 1
            slots.add(freq)
        return res
