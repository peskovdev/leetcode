class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        res = []
        fp, sp = 0, 0
        while fp < len(nums1) and sp < len(nums2):
            if nums1[fp] < nums2[sp]:
                fp += 1
            elif nums1[fp] > nums2[sp]:
                sp += 1
            else:  # equal
                res.append(nums1[fp])
                fp, sp = fp + 1, sp + 1
        return res
