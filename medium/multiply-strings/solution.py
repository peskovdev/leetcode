class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                product = int(n1) * int(n2) + num[i + j]
                num[i + j] = product % 10
                num[i + j + 1] += product // 10
        res = []
        for n in reversed(num):
            if n or res:
                res.append(n)
        return "".join([str(n) for n in res]) if res else "0"
