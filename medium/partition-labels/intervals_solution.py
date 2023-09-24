class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        count = [[-1, -1] for _ in range(26)]  # [start, end]
        for i, c in enumerate(s):
            if count[ord(c) - ord("a")][0] == -1:
                count[ord(c) - ord("a")][0] = i
            count[ord(c) - ord("a")][1] = i

        res = []
        i, start = 0, 0
        while i < len(s):
            i, can = self.can_cut(i, count)
            if can:
                res.append(i - start)
                start = i
        return res

    def can_cut(self, i, count) -> tuple[int, bool]:
        for start, end in count:
            if start <= i < end:
                return end, False
        return i + 1, True
