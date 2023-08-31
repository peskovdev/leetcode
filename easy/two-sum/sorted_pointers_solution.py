class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(nums)
        l_pointer = 0
        r_pointer = len(nums) - 1
        while l_pointer < r_pointer:
            current_sum = sorted_nums[l_pointer] + sorted_nums[r_pointer]
            if current_sum == target:
                break
            elif current_sum > target:
                r_pointer -= 1
            else:
                l_pointer += 1

        # return [sorted_nums[l_pointer], sorted_nums[r_pointer]]
        left_index = nums.index(sorted_nums[l_pointer])
        right_index = nums.index(sorted_nums[r_pointer])
        if left_index == right_index:
            right_index = nums.index(sorted_nums[r_pointer], left_index + 1)
        return [left_index, right_index]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))
