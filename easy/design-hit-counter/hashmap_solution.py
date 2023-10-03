class HitCounter:
    def __init__(self):
        self.count = {}

    def hit(self, timestamp: int):
        self.count[timestamp] = self.count.get(timestamp, 0) + 1

    def get_hits(self, timestamp: int) -> int:
        res = 0
        for time in sorted(self.count):
            if timestamp - time >= 300:
                continue
            elif time > timestamp:
                break
            else:
                res += self.count[time]
        return res
