class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res: list[str] = []
        for i in range(1, n + 1):
            res_str = ""
            if i % 3 == 0:
                res_str += "Fizz"
            if i % 5 == 0:
                res_str += "Buzz"
            if not res_str:
                res_str += str(i)
            res.append(res_str)
        return res


sol = Solution()
print(sol.fizzBuzz(3))
print(sol.fizzBuzz(5))
print(sol.fizzBuzz(15))
