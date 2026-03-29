class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        result = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = price - min_price
            
            if result < max_profit:
                result = max_profit
        return result