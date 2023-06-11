class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        for i, customer in enumerate(accounts):
            accounts[i] = sum(customer)

        return max(accounts)


sol = Solution()
print(sol.maximumWealth([[1, 2, 3], [3, 2, 1]]))
print(sol.maximumWealth([[1, 5], [7, 3], [3, 5]]))
print(sol.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
