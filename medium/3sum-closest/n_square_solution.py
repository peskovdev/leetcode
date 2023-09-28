class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            lp, rp = i + 1, len(nums) - 1
            while lp < rp:
                cur = nums[i] + nums[lp] + nums[rp]
                if cur < target:
                    lp += 1
                else:
                    rp -= 1
                if abs(target - res) > abs(target - cur):
                    res = cur
        return res
