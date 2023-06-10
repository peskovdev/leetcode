class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened_num = 0
        output = []
        position = 1
        for i, char in enumerate(s):
            if char == "(":
                opened_num += 1
            else:
                opened_num -= 1
                if opened_num == 0:
                    output.append(s[position:i])
                    position = i + 2
                    opened_num = 0
        return "".join(output)


sol = Solution()
print(sol.removeOuterParentheses("(()())(())"))
print(sol.removeOuterParentheses("(()())(())(()(()))"))
print(sol.removeOuterParentheses("()()"))
