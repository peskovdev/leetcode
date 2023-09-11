class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = sorted([z for z in zip(position, speed)], key=lambda k: k[0])

        prev_time = 0.0
        fleet = len(position)
        while stack:
            pos, sp = stack.pop()
            time_to_finish = (target - pos) / sp
            if time_to_finish <= prev_time:
                fleet -= 1
            else:
                prev_time = time_to_finish
        return fleet
