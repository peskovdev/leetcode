class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1, set2 = set(nums1), set(nums2)

        for n in set1.copy():
            if n in set2:
                set1.remove(n)
                set2.remove(n)

        return [list(set1), list(set2)]
