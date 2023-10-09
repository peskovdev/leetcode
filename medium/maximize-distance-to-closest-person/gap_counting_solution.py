import math


class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        cur, res = 0, 0
        for n in seats:
            if n == 0:
                cur += 1
            else:
                cur = 0
            res = max(res, math.ceil(cur / 2))

        for lcand, n in enumerate(seats):
            if n == 1: break
        for rcand, n in enumerate(seats[::-1]):
            if n == 1: break

        return max(res, lcand, rcand)
