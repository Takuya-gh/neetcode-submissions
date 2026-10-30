class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        maxP = 0
        while sell <= len(prices) - 1:
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxP = max(profit, maxP)
            else:
                buy = sell
            sell += 1
        return maxP


"""
two pointers
if profit > max profit, update max profit
"""