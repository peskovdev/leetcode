from collections import deque
from typing import Deque


class RecentCounter:
    def __init__(self):
        self.q: Deque = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while (t - 3000) > self.q[0]:
            self.q.popleft()
        return len(self.q)
