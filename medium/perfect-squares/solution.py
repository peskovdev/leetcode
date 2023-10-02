class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [n] * n
        squares = []

        for s in range(1, int(n**0.5) + 1):
            square = s**2
            if square > n:
                break
            squares.append(square)

        for target in range(1, n + 1):
            for square in squares:
                if square > target:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        return dp[n]
