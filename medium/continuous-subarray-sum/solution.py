class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainders = {0: -1}

        prefix = 0
        for i, n in enumerate(nums):
            prefix += n
            r = prefix % k
            if r in remainders:
                if i - remainders[r] >= 2:
                    return True
            else:
                remainders[r] = i
        return False
