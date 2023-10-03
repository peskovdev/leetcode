class HitCounter:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int):
        self.hits.append(timestamp)

    def get_hits(self, timestamp: int) -> int:
        target = timestamp - 300
        lp, rp = 0, len(self.hits) - 1
        while lp <= rp:
            middle = (lp + rp) // 2
            if target >= self.hits[middle]:
                lp = middle + 1
            else:
                rp = middle - 1

        return len(self.hits) - lp
