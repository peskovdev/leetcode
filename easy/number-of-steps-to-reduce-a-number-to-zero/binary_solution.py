class Solution:
    def numberOfSteps(self, num: int) -> int:
        operations = 0
        while num > 0:
            if num & 1:  # 11110 & 00001 = 00000 (0=false - not even (or odd) )
                num = num ^ 1
            else:  # even
                num = num >> 1
            operations += 1
        return operations


sol = Solution()
print(sol.numberOfSteps(1000))
print(sol.numberOfSteps(6))
