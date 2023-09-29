class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lp, rp = 0, len(nums) - 1
        index = -1
        while lp <= rp:
            mp = (lp + rp) // 2
            if target < nums[mp]:
                rp = mp - 1
            elif target > nums[mp]:
                lp = mp + 1
            else:
                index = mp
                break
        if index == -1:
            return [-1, -1]

        lp, rp = index, index
        while lp > 0 and nums[lp] == nums[lp - 1]:
            lp -= 1
        while rp + 1 < len(nums) and nums[rp] == nums[rp + 1]:
            rp += 1
        return [lp, rp]
