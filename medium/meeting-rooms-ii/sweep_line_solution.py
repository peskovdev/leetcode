class Solution:
    def min_meeting_rooms(self, intervals: list[list[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        sp, ep = 0, 0  # start&end pointers
        res, rooms = 0, 0
        while sp < len(starts):
            if starts[sp] < ends[ep]:
                rooms += 1
                sp += 1
            else:
                rooms -= 1
                ep += 1
            res = max(res, rooms)
        return res
