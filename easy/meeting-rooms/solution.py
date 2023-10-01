class Solution:
    def can_attend_meetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda pair: pair[0])

        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                return False
        return True
