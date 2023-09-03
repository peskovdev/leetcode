class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        bracket_pairs = {
            "]": "[",
            ")": "(",
            "}": "{",
        }

        for c in s:
            if c in bracket_pairs:  # keys of hashmap is closing bracket
                if len(stack) == 0:
                    return False
                if bracket_pairs[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
