class Solution:
    def is_reflected(self, points: list[list[int]]) -> bool:
        if not points:
            return True

        original = set([tuple(p) for p in points])
        mx = max(original, key=lambda point: point[0])[0]
        mn = min(original, key=lambda point: point[0])[0]
        median = mn + (mx - mn) / 2

        reflected = set()
        for x, y in original:
            distance = abs(median - x)
            if x > median:
                x -= distance * 2
            else:
                x += distance * 2
            reflected.add((x, y))

        return original == reflected
