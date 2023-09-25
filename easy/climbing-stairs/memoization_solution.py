class Solution:
    def climbStairs(self, n: int) -> int:
        visited: dict[int, int] = {}

        def dfs(pos):
            if pos in visited:
                return visited[pos]
            if pos > n:
                return 0
            if pos == n:
                return 1
            visited[pos] = dfs(pos + 1) + dfs(pos + 2)
            return visited[pos]
        return dfs(0)
