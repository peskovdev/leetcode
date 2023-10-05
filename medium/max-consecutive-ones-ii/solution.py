from typing import List


class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """

    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        lp = 0
        zeros = []
        res = 0
        for rp, n in enumerate(nums):
            if n == 0:
                zeros.append(rp)
            if len(zeros) == 2:
                lp = zeros.pop(0) + 1
            res = max(res, (rp - lp + 1))
        return res
