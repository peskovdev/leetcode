class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res: list[str] = []
        for i in range(1, n + 1):
            div_by_3 = i % 3 == 0
            div_by_5 = i % 5 == 0
            if div_by_3 and div_by_5:
                res_str = "".join(["FizzBuzz"])
            elif div_by_3:
                res_str = "".join(["Fizz"])
            elif div_by_5:
                res_str = "".join(["Buzz"])
            else:
                res_str = "".join([str(i)])
            res.append(res_str)
        return res


sol = Solution()
print(sol.fizzBuzz(3))
print(sol.fizzBuzz(5))
print(sol.fizzBuzz(13))
