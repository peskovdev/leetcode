class Solution:
    def findMin(self, nums: list[int]) -> int:
        lp, rp = 0, len(nums) - 1
        shift = (lp + rp) // 2

        prev_num = nums[lp]
        while nums[lp] > nums[rp]:
            if prev_num < nums[lp]:
                lp = (lp + shift) % len(nums)
                rp = (rp + shift) % len(nums)
            else:
                lp -= shift
                rp -= shift
                if lp < 0:
                    lp = len(nums) + lp
                if rp < 0:
                    rp = len(nums) + rp
            prev_num = nums[lp]
            shift = max(1, shift // 2)

        return nums[lp]
