class Solution:
    def min_meeting_rooms(self, intervals: list[list[int]]) -> int:
        time = []  # pair: [time, action]
        for i in intervals:
            time.append((i[0], +1))
            time.append((i[1], -1))
        time.sort(key=lambda pair: pair[0])

        res, rooms = 0, 0
        for t in time:
            rooms += t[1]
            res = max(res, rooms)
        return res
