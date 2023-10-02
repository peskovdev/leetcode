class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        lp = 0
        for rp in range(len(nums)):
            if nums[rp] != 0:
                nums[lp], nums[rp] = nums[rp], nums[lp]
                lp += 1
