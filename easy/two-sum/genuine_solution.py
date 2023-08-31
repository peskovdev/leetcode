class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashdict: dict = {}
        for i, number in enumerate(nums):
            value = target - number
            if hashdict.get(value) is not None:
                return [i, nums.index(value)]
            hashdict[number] = value
        return []  # this code won't be executed by task definition (added for mypy)
