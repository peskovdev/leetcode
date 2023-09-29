class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lp = self.binary_search(nums, target, True)
        rp = self.binary_search(nums, target, False)
        return[lp, rp]

    def binary_search(self, nums, target, lbias):
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
                if lbias:
                    rp = mp - 1
                else:
                    lp = mp + 1
        return index
