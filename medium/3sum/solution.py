class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i, el in enumerate(nums):
            if i > 0:
                if el == nums[i - 1]:
                    continue

            lp, rp = i + 1, len(nums) - 1

            while lp < rp:
                current_sum = el + nums[lp] + nums[rp]
                if current_sum < 0:
                    lp += 1
                elif current_sum > 0:
                    rp -= 1
                else:
                    result.append((el, nums[lp], nums[rp]))
                    lp += 1
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1

        return result  # type: ignore
