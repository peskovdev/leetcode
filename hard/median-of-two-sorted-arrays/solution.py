class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n = len(nums1) + len(nums2)
        half = n // 2
        if len(nums1) > len(nums2):  # ensure that nums1 is a smaller part
            nums1, nums2 = nums2, nums1

        lp, rp = 0, len(nums1) - 1
        while True:
            i = (lp + rp) // 2
            j = half - i - 2

            n1Left = nums1[i] if i >= 0 else float("-inf")
            n1Right = nums1[i + 1] if (i + 1) < len(nums1) else float("inf")
            n2Left = nums2[j] if j >= 0 else float("-inf")
            n2Right = nums2[j + 1] if (j + 1) < len(nums2) else float("inf")

            if n1Left <= n2Right and n2Left <= n1Right:
                if n % 2 == 1:
                    return min(n1Right, n2Right)
                return (max(n1Left, n2Left) + min(n1Right, n2Right)) / 2
            elif n1Left > n2Right:
                rp = i - 1
            else:
                lp = i + 1
