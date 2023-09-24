from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(row, col):
            visited.add((row, col))
            q = deque([(row, col)])
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        0 <= r < rows and 0 <= c < cols
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        return res
