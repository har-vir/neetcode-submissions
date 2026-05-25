class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            profit = 0

        profit = 0
        minPrice = prices[0]
        l = 0

        while l < len(prices):
            if prices[l] < minPrice:
                minPrice = prices[l]
            
            if (prices[l] - minPrice) > profit:
                profit = prices[l] - minPrice

            l += 1
        
        return profit