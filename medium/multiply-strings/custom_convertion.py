class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return self.make_str(self.make_int(num1) * self.make_int(num2))

    def make_int(self, s: str) -> int:
        num = 0
        for c in s:
            num *= 10
            num += int(c)
        return num

    def make_str(self, num: int) -> str:
        if num == 0:
            return "0"

        res = []
        while num > 0:
            res.append(str(num % 10))
            num = num // 10
        return "".join(res[::-1])
