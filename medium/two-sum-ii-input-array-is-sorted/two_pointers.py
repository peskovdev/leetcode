class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lp, rp = 0, len(numbers) - 1

        while lp < rp:
            current_sum = numbers[lp] + numbers[rp]
            if current_sum < target:
                lp += 1
            elif current_sum > target:
                rp -= 1
            else:  # current_sum == target
                break

        return [lp + 1, rp + 1]
