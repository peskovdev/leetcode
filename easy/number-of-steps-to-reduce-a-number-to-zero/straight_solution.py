class Solution:
    def numberOfSteps(self, num: int) -> int:
        operations = 0
        while num > 0:
            if num % 2 != 0:
                num -= 1
            else:
                num /= 2
            operations += 1
        return operations


sol = Solution()
print(sol.numberOfSteps(1000))
print(sol.numberOfSteps(6))
