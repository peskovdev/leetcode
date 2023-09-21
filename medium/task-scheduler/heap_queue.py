import heapq
from collections import Counter, deque
from typing import Deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        maxheap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxheap)
        q: Deque[[int, int]] = deque()  # [time, -cnt]
        time = 0
        while maxheap or q:
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    q.append((time + n, cnt))
            time += 1
            if q and time > q[0][0]:
                heapq.heappush(maxheap, q.popleft()[1])
        return time


sol = Solution()
print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(sol.leastInterval(["A", "A", "A", "A", "B", "B", "C"], 2))
print(sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
print(sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
