class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            sum_wealth = sum(customer)
            if max_wealth < sum_wealth:
                max_wealth = sum_wealth

        return max_wealth


sol = Solution()
print(sol.maximumWealth([[1, 2, 3], [3, 2, 1]]))
print(sol.maximumWealth([[1, 5], [7, 3], [3, 5]]))
print(sol.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
