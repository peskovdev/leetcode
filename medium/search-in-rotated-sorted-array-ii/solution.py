class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            mp = (lp + rp) // 2
            if nums[mp] == target:
                return True
            elif nums[mp] > nums[rp] or nums[mp] > nums[lp]:  # left sorted portion
                if nums[lp] <= target < nums[mp]:
                    rp = mp - 1
                else:
                    lp = mp + 1
            elif nums[mp] < nums[lp] or nums[mp] < nums[rp]:  # right sorted portion
                if nums[mp] < target <= nums[rp]:
                    lp = mp + 1
                else:
                    rp = mp - 1
            else:  # equal
                rp -= 1
        return False
