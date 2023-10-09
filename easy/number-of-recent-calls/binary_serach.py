class RecentCounter:
    def __init__(self):
        self.calls = []

    def ping(self, t: int) -> int:
        self.calls.append(t)
        target = t - 3000
        lp, rp = 0, len(self.calls) - 1

        while lp <= rp:
            mp = (lp + rp) // 2
            if target > self.calls[mp]:
                lp = mp + 1
            elif target < self.calls[mp]:
                rp = mp - 1
            else:
                lp = mp
                break

        return len(self.calls) - lp
