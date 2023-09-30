"""
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
"""


class Solution:
    def length_of_longest_substring_two_distinct(self, s: str) -> int:
        chars_last_index: dict[str, int] = {}
        lp, res = 0, 0
        for rp, c in enumerate(s):
            chars_last_index[c] = rp

            if len(chars_last_index) > 2:
                char, index = min(chars_last_index.items(), key=lambda x: x[1])
                del chars_last_index[char]
                lp = index + 1

            res = max(res, (rp - lp + 1))
        return res


sol = Solution()

inp = "eceba"
res = sol.length_of_longest_substring_two_distinct(inp)
assert res == 3, f"input: {inp}, expected: 3, res: {res}"

inp = "baece"
res = sol.length_of_longest_substring_two_distinct(inp)
assert res == 3, f"input: {inp}, expected: 3, res: {res}"

inp = "aaa"
res = sol.length_of_longest_substring_two_distinct(inp)
assert res == 3, f"input: {inp}, expected: 3, res: {res}"

inp = "abaaacaa"
res = sol.length_of_longest_substring_two_distinct(inp)
assert res == 6, f"input: {inp}, expected: 6, res: {res}"

inp = "ccaabbb"
res = sol.length_of_longest_substring_two_distinct(inp)
assert res == 5, f"input: {inp}, expected: 5, res: {res}"
