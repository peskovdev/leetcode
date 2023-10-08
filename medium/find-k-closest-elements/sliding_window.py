class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        lp, rp = 0, len(arr) - k

        while lp < rp:
            mp = (lp + rp) // 2

            if x - arr[mp] > arr[mp + k] - x:
                lp = mp + 1
            else:
                rp = mp

        return arr[lp: lp + k]
