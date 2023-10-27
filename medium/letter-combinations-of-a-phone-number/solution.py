class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        s: list[str] = []

        def backtrack(idx):
            if idx == len(digits):
                res.append("".join(s))
                return
            for c in mapping[digits[idx]]:
                s.append(c)
                backtrack(idx + 1)
                s.pop()

        if digits:
            backtrack(0)
        return res
