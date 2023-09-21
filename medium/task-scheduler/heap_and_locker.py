import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        maxheap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxheap)

        time = 0
        while maxheap:
            popped_items: list[int] = []
            for _ in range(n + 1):
                if maxheap == popped_items == []:
                    break
                if maxheap:
                    cnt = 1 + heapq.heappop(maxheap)
                    if cnt:
                        popped_items.append(cnt)
                time += 1
            for cnt in popped_items:
                heapq.heappush(maxheap, cnt)
        return time


sol = Solution()
print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(sol.leastInterval(["A", "A", "A", "A", "B", "B", "C"], 2))
print(sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
print(sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
