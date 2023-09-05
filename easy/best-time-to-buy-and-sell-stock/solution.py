class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = float("inf")
        max_profit = 0

        for sell_price in prices:
            if sell_price < buy_price:
                buy_price = sell_price
                continue

            xprofit = sell_price - buy_price
            max_profit = max(max_profit, xprofit)  # type: ignore

        return max_profit
