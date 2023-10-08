from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        buckets: list[list] = [[]] + [[] for _ in range(len(words))]

        for s, freq in Counter(words).items():
            buckets[freq].append(s)

        res = []
        for bucket in buckets[::-1]:
            for word in sorted(bucket):
                res.append(word)
                if len(res) == k:
                    return res
        return res
