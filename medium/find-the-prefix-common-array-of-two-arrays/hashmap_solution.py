class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        cnt: dict[int, int] = {}
        common = 0
        res = []
        for i in range(len(A)):
            cnt[A[i]] = cnt.get(A[i], 0) + 1
            cnt[B[i]] = cnt.get(B[i], 0) + 1
            if A[i] == B[i]:
                common += 1
            else:
                if cnt[A[i]] == 2:
                    common += 1
                if cnt[B[i]] == 2:
                    common += 1
            res.append(common)
        return res
