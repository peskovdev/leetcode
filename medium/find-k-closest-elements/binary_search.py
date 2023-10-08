class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        lp, rp = 0, len(arr) - 1
        idx, res_diff = 0, abs(x - arr[0])
        while lp <= rp:
            mp = (lp + rp) // 2
            cur_diff = abs(x - arr[mp])
            if cur_diff < res_diff or (cur_diff == res_diff and mp < idx):
                idx, res_diff = mp, cur_diff

            if x < arr[mp]:
                rp = mp - 1
            elif x > arr[mp]:
                lp = mp + 1
            else:
                break

        lp = rp = idx
        for _ in range(k - 1):
            if lp == 0:
                rp += 1
            elif rp == (len(arr) - 1) or abs(x - arr[lp - 1]) <= abs(x - arr[rp + 1]):
                lp -= 1
            else:
                rp += 1

        return arr[lp: rp + 1]
