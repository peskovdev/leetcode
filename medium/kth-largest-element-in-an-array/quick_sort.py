class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(lp, rp):
            pivot, p = nums[rp], lp
            for i in range(lp, rp):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[rp] = pivot, nums[p]
            if k > p:
                return quick_select(p + 1, rp)
            elif k < p:
                return quick_select(lp, p - 1)
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)
