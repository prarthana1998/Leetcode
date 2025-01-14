class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        left = prices[0]
        n = len(prices)
        for right in range(1,n):
            max_profit = max(max_profit, prices[right] - left)
            left = min(prices[right], left)

        return max_profit
            
            
        