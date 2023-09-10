import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lp, rp = 1, max(piles)
        res = rp

        while lp <= rp:
            k = (lp + rp) // 2  # eating speed
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)
                if total_time > h:
                    break

            if total_time <= h:
                res = k
                rp = k - 1
            else:
                lp = k + 1

        return res
