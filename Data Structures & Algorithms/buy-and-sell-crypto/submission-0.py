class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if buyPrice > price:
                buyPrice = price
            maxProfit = max(maxProfit,price - buyPrice)
        
        return maxProfit