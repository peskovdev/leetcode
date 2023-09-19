import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            z = -(x - y)
            if z != 0:
                heapq.heappush(stones, z)
        return -stones[0] if stones else 0
