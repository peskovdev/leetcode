class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res: list[str] = []

        def backtrack(stack: list[str], open: int, close: int):
            if open == close == n:
                res.append("".join(stack))
                return

            if open != n:
                backtrack(stack=stack+["("], open=open + 1, close=close)
            if close < open:
                backtrack(stack=stack+[")"], open=open, close=close + 1)

        backtrack(stack=[], open=0, close=0)
        return res
