class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashdict: dict = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in hashdict:
                return [index, hashdict[diff]]
            hashdict[number] = index
        return []  # this code won't be executed by task definition (added for mypy)
