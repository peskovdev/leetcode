class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set(nums)
        return len(hashset) != len(nums)
