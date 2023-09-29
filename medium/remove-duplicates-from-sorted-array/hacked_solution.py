class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
          s = set(nums)
          nums.clear()
          for i in s:
               nums.append(i)
          nums.sort()
          return len(nums)
