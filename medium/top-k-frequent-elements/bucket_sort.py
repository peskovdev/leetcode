from typing import List, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter: dict[int, int] = Counter(nums)  # {num: frequency}

        buckets: list[list] = [[] for i in range(len(nums) + 1)]
        for key, val in counter.items():
            buckets[val].append(key)

        res: list = []
        for i in range(len(buckets)-1, 0, -1):
            for number in buckets[i]:
                res.append(number)
                if len(res) == k:
                    return res
        return res
