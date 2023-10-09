import math


class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        lp = -1
        res = 0
        for rp in range(len(seats)):
            if seats[rp] == 1:
                res = max(res, math.ceil((rp - lp) / 2))
                lp = rp + 1
            if lp == -1:
                res = max(res, rp + 1)
        res = max(res, (rp - lp + 1))

        return res
