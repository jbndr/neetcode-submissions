class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        buy_in = -1

        for right in range(len(prices)):
            if buy_in == -1:
                buy_in = prices[right]

            if prices[right] < buy_in:
                buy_in = prices[right]
            else:
                profit = max(profit, prices[right] - buy_in)

        return profit

        
        