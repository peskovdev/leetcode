class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while carry or i >= 0 or j >= 0:
            v1 = int(num1[i]) if i >= 0 else 0
            v2 = int(num2[j]) if j >= 0 else 0
            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10
            res.append(str(val))
            i, j = i - 1, j - 1

        return "".join(res[::-1])
