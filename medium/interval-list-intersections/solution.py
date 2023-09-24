class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        res = []
        fp, sp = 0, 0
        while fp < len(firstList) and sp < len(secondList):
            start = max(firstList[fp][0], secondList[sp][0])
            end = min(firstList[fp][1], secondList[sp][1])
            if start <= end:
                res.append([start, end])
            if firstList[fp][1] < secondList[sp][1]:
                fp += 1
            else:
                sp += 1
        return res
