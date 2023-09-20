import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minheap: list[[int, list[int]]] = []
        for point in points:
            distance = (point[0] ** 2) + (point[1] ** 2)
            minheap.append([distance, point])
        heapq.heapify(minheap)
        return [heapq.heappop(minheap)[1] for _ in range(k)]
