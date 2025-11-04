class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0 #indices
        high = 0

        profit = 0
        for current in range(len(prices)):
            if(prices[current] > prices[high]): #update highest relative price
                high = current
            if(prices[low] > prices[current]): #update low and high
                profit = max(profit, prices[high] - prices[low])
                low = current
                high = current
        return max(profit, prices[high] - prices[low])

        
