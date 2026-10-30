class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxP = 0
        for sell in range(len(prices)):
            profit = prices[sell] - prices[buy]
            if prices[sell] > prices[buy]:
                maxP = max(profit, maxP)
            else:
                buy = sell
            sell += 1
        return maxP