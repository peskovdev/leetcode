class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            mp = (lp + rp) // 2

            if target < nums[mp]:
                if nums[rp] < nums[lp] and nums[mp] > nums[rp] >= target:
                    lp = mp + 1
                else:
                    rp = mp - 1
            elif target > nums[mp]:
                if nums[lp] > nums[rp] and nums[mp] < nums[lp] <= target:
                    rp = mp - 1
                else:
                    lp = mp + 1
            else:
                return mp

        return -1
