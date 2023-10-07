class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        stack: list[[int, int]] = []  # pair: [index, number]
        lp, mx = len(nums), float("-inf")
        for i, n in enumerate(nums):
            while stack and stack[-1][1] > n:
                cand = stack.pop()
                lp = min(lp, cand[0])
                mx = max(mx, cand[1])
            stack.append((i, n))

        if lp == len(nums):
            return 0

        for rp in range(len(nums) - 1, -1, -1):
            if nums[rp] < mx:
                break
        return rp - lp + 1
