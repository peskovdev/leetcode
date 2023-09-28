class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            lsum = nums[i] + nums[i + 1] + nums[i + 2]
            rsum = nums[i] + nums[-1] + nums[-2]
            res = min([res, lsum, rsum], key=lambda x: abs(target - x))

            if lsum < target < rsum:
                lp, rp = i + 1, len(nums) - 1
                while lp < rp:
                    cur = nums[i] + nums[lp] + nums[rp]
                    if cur < target:
                        lp += 1
                    else:
                        rp -= 1
                    res = min([res, cur], key=lambda x: abs(target - x))
        return res
