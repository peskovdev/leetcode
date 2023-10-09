class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        val, idx = float("inf"), 0
        lp, rp = 0, len(nums) - 1
        while lp <= rp:
            mp = (lp + rp) // 2
            if abs(nums[mp]) < val:
                val, idx = abs(nums[mp]), mp
            if 0 > nums[mp]:
                lp = mp + 1
            elif 0 < nums[mp]:
                rp = mp - 1
            else:
                break

        # Or finding idx of lowest by module with brute force
        # idx = nums.index(min(nums, key=lambda n: abs(n)))
        lp, rp = idx, idx + 1
        res = []
        while lp >= 0 or rp < len(nums):
            if rp == len(nums) or abs(nums[lp]) < abs(nums[rp]):
                res.append(nums[lp] ** 2)
                lp -= 1
            else:
                res.append(nums[rp] ** 2)
                rp += 1

        return res
