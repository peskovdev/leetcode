class ZigzagIterator:
    def __init__(self, v1, v2) -> None:
        self.v1, self.v2 = v1, v2
        self.p1, self.p2 = 0, 0
        self.v1_bias = True if v1 else False

    def _next(self) -> int:
        if self.v1_bias:
            self.v1_bias = False if self.p2 < len(self.v2) else True
            val = self.v1[self.p1]
            self.p1 += 1
        else:
            self.v1_bias = True if self.p1 < len(self.v1) else False
            val = self.v2[self.p2]
            self.p2 += 1
        return val

    def hasNext(self) -> bool:
        return self.p1 < len(self.v1) or self.p2 < len(self.v2)
