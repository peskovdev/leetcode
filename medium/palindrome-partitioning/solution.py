class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        part: list[str] = []
        cached_palis = set()

        def backtrack(start):
            if start == len(s):
                res.append(part.copy())
                return
            for i in range(start, len(s)):
                substring = s[start: i + 1]
                if substring in cached_palis or substring == substring[::-1]:
                    cached_palis.add(substring)
                    part.append(substring)
                    backtrack(i + 1)
                    part.pop()
        backtrack(0)
        return res
