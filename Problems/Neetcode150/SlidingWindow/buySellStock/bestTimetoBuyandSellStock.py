class Solution:
    def maxProfit(self, prices):
        l, r = 0, 1
        
        Ansprofit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                Ansprofit = max(profit, Ansprofit)
            else:
                l = r
            r += 1
            
        return Ansprofit