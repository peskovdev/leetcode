class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            if nums[lp] < nums[rp]:
                res = min(res, nums[lp])
                break

            mp = (lp + rp) // 2
            res = min(res, nums[mp])

            if nums[lp] <= nums[mp]:
                lp = mp + 1
            else:
                rp = mp - 1

        return res
