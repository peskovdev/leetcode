class Solution:
    def findMin(self, nums: list[int]) -> int:
        lp, rp = 0, len(nums) - 1

        while lp < rp:
            mp = (lp + rp) // 2
            if nums[mp] > nums[rp]:
                lp = mp + 1
            elif nums[mp] < nums[lp]:
                rp = mp
            else:
                rp -= 1

        return nums[lp]
