class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        lp = 0
        for rp in range(len(nums)):
            if nums[rp] % 2 == 0:
                nums[lp], nums[rp] = nums[rp], nums[lp]
                lp += 1
        return nums
