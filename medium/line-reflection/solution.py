class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """

    def is_reflected(self, points: list[list[int]]) -> bool:
        if not points:
            return True

        points.sort(key=lambda point: point[0])  # by x

        middle = points[0][0] + (points[-1][0] - points[0][0]) / 2
        lp, rp = 0, len(points) - 1
        while lp < rp:
            left, right = points[lp], points[rp]
            if left[1] != right[1] or (middle - left[0]) != (right[0] - middle):
                return False
            lp += 1
            rp -= 1
        return points[lp][0] == middle if lp == rp else True
