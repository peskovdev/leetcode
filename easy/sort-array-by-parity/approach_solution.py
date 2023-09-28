class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        lp, rp = 0, len(nums) - 1

        while lp < rp:
            while lp < rp and nums[lp] % 2 != 1:
                lp += 1
            while lp < rp and nums[rp] % 2 != 0:
                rp -= 1
            nums[lp], nums[rp] = nums[rp], nums[lp]
        return nums
