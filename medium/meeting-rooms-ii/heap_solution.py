import heapq


class Solution:
    def min_meeting_rooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms: list[int] = []  # minheap contains end_time
        for i in range(len(intervals)):
            if rooms and rooms[0] <= intervals[i][0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        return len(rooms)
