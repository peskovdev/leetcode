class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res: list[str] = []
        for i in range(1, n + 1):
            div_by_3 = i % 3 == 0
            div_by_5 = i % 5 == 0
            if div_by_3 and div_by_5:
                res.append("FizzBuzz")
            elif div_by_3:
                res.append("Fizz")
            elif div_by_5:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


sol = Solution()
print(sol.fizzBuzz(3))
print(sol.fizzBuzz(5))
print(sol.fizzBuzz(13))
