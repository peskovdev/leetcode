class Solution:
    def findRLEArray(self, encoded1: list[list[int]], encoded2: list[list[int]]) -> list[list[int]]:
        res: list[[int, int]] = []

        i, j = 0, 0
        while i < len(encoded1) and j < len(encoded2):
            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]

            product = val1 * val2
            freq = min(freq1, freq2)

            if res and product == res[-1][0]:
                res[-1][1] += freq
            else:
                res.append([product, freq])

            encoded1[i][1] -= freq
            encoded2[j][1] -= freq

            if freq1 == freq:
                i += 1
            if freq2 == freq:
                j += 1

        return res


sol = Solution()

inp = [[[1, 3], [2, 3]], [[6, 3], [3, 3]]]
exp = [[6, 6]]
"""
1 1 1 2 2 2
6 6 6 3 3 3
===========
6 6 6 6 6 6
"""
res = sol.findRLEArray(*inp)
assert res == exp, f"\nAr1={inp[0]}, Ar2={inp[1]}\nExpected: {exp},\nReturned: {res}"

inp = [[[1, 3], [2, 1], [3, 2]], [[2, 3], [3, 3]]]
exp = [[2, 3], [6, 1], [9, 2]]
"""
1 1 1 2 3 3
2 2 2 3 3 3
===========
2 2 2 6 9 9
"""
res = sol.findRLEArray(*inp)
assert res == exp, f"\nAr1={inp[0]}, Ar2={inp[1]}\nExpected: {exp},\nReturned: {res}"


inp = [[[1, 4], [2, 2], [3, 1]], [[7, 2], [9, 3], [5, 1], [4, 1]]]
exp = [[7, 2], [9, 2], [18, 1], [10, 1], [12, 1]]
"""
1 1 1 1  2  2  3
7 7 9 9  9  5  4
================
7 7 9 9 18 10 12
"""
res = sol.findRLEArray(*inp)
assert res == exp, f"\nAr1={inp[0]}, Ar2={inp[1]}\nExpected: {exp},\nReturned: {res}"
