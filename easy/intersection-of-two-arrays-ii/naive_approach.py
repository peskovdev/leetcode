from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count1 = Counter(nums1)
        res: list[int] = []

        for num in nums2:
            if num in count1 and count1[num] > 0:
                res.append(num)
                count1[num] -= 1
        return res
