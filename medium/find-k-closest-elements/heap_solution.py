import heapq


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        minheap = []
        for n in arr:
            minheap.append((abs(n - x), n))
        heapq.heapify(minheap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return sorted(res)
