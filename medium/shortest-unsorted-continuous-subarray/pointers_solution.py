class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        mx, rp = nums[0], -1
        for i in range(1, len(nums)):
            if nums[i] < mx:
                rp = i
            else:
                mx = nums[i]

        mn, lp = nums[-1], -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > mn:
                lp = i
            else:
                mn = nums[i]

        return (rp - lp + 1) if lp != rp else 0
