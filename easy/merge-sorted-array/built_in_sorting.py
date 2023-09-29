class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(m, len(nums1)):
            nums1[i] = nums2.pop()
        nums1.sort()
