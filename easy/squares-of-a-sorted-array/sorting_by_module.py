class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        nums.sort(key=lambda n: abs(n))
        return [n ** 2 for n in nums]
