class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        seta, setb = set(), set()
        common = set()
        res = []
        for i in range(len(A)):
            seta.add(A[i])
            setb.add(B[i])

            if A[i] in setb:
                common.add(A[i])
            if B[i] in seta:
                common.add(B[i])
            res.append(len(common))

        return res
