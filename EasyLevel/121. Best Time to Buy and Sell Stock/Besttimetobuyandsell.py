class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leastprice = prices[0]
        n = len(prices)
        maxprofit = 0
        for i in range(1,n):
            if prices[i] < leastprice:
                leastprice = prices[i]
            elif prices[i]-leastprice > maxprofit:
                maxprofit = prices[i]-leastprice        
        return maxprofit
