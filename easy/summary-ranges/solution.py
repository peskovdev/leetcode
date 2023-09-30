class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res, rang = [], []
        for i in range(len(nums)):
            rang.append(nums[i])
            if (i + 1 < len(nums) and nums[i + 1] - nums[i] != 1) or i == len(nums) - 1:
                if len(rang) > 1:
                    res.append(f"{rang[0]}->{rang[-1]}")
                else:
                    res.append(str(rang[0]))
                rang = []
        return res
