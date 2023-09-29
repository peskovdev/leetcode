class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        lp = 1
        for rp in range(1, len(nums)):
            if nums[rp] != nums[rp - 1]:
                nums[lp] = nums[rp]
                lp += 1
        return lp
