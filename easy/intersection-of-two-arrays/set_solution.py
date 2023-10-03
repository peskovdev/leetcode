class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1, set2 = set(nums1), set(nums2)

        long = set1 if len(set1) > len(set2) else set2
        short = set2 if long is set1 else set1
        res = []
        for num in short:
            if num in long:
                res.append(num)
        return res
