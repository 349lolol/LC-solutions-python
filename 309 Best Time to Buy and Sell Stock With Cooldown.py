class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if(n == 1): 
            return 0
        hold = [0] * n
        empty  = [0] * n
        hold [0] = -prices[0]
        hold [1] = max(hold[0], -prices[1]) 
        empty [1] = max(0, hold[0] + prices[1])
        own = hold[1] > empty[1]
        #each day, see if holding from the day before is better, or if 
        #selling 2 days before and buying today is better 
        #for selling, see if being empty is better or if selling today is better
        for i in range(2, n):
            hold[i] = max(hold[i-1], empty[i-2] - prices[i])
            empty[i] = max(empty[i-1], hold[i-1] + prices[i])

        return max(hold[n-1], empty[n-1])
        

        
