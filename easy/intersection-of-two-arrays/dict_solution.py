from collections import Counter


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count1, count2 = Counter(nums1), Counter(nums2)

        long = count1 if len(count1) > len(count2) else count2
        short = count2 if long is count1 else count1

        res = []
        for num in short:
            if long.get(num):
                res.append(num)
        return res
