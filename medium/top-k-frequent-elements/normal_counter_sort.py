from typing import List, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return sorted(counter, key=lambda key: counter[key], reverse=True)[:k]
