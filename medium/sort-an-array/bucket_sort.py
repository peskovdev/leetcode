class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        max_val = max(nums)
        min_val = min(nums)
        buckets = [0] * (max_val - min_val + 1)

        for i, n in enumerate(nums):
            buckets[n - min_val] += 1

        res = []
        for i, bucket in enumerate(buckets):
            if bucket != 0:
                res.extend([i + min_val] * bucket)
        return res
