class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remainders = {0: 1}
        res, pr_sum = 0, 0
        for n in nums:
            pr_sum += n
            r = pr_sum % k

            if r in remainders:
                res += remainders[r]
            remainders[r] = remainders.get(r, 0) + 1

        return res
