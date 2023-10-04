class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        n = len(prices)
        maxprofit = 0
        for i in range(1,n):
            if prices[i] < least:
                least = prices[i]
            elif prices[i]-least > maxprofit:
                maxprofit = prices[i]-least        
        return maxprofit