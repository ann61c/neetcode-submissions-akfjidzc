class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low_price = prices[0]
        profit = 0
        max_profit = 0
        for price in prices:
            if price <= low_price:
                low_price = price
            elif price > low_price:
                profit = price - low_price
            max_profit = max(max_profit, profit)
        return max_profit