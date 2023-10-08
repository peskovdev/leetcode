import heapq
from collections import Counter


class HeapWord:
    def __init__(self, word):
        self.word = word

    def __gt__(self, other):
        return self.word < other.word


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        minheap: list[[int, HeapWord]] = []
        for w, freq in Counter(words).items():
            word = HeapWord(w)
            heapq.heappush(minheap, (freq, word))
            while len(minheap) > k:
                heapq.heappop(minheap)

        maxheap = [(-freq, w.word) for freq, w in minheap]
        heapq.heapify(maxheap)

        res: list[str] = []
        while len(res) != k:
            res.append(heapq.heappop(maxheap)[1])
        return res
