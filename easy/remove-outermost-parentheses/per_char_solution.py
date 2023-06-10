class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        opened_num = 0
        for char in s:
            if char == "(":
                if opened_num > 0:
                    result.append(char)
                opened_num += 1
            else:
                if opened_num > 1:
                    result.append(char)
                opened_num -= 1
        return "".join(result)


sol = Solution()
print(sol.removeOuterParentheses("(()())(())"))
print(sol.removeOuterParentheses("(()())(())(()(()))"))
print(sol.removeOuterParentheses("()()"))
