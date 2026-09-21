class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = [0]
        L = len(prices)
        for i in range(0, L):
            for j in range(i, L):
                profit = prices[j] - prices[i]
                if profit > max(profit_list):
                    profit_list.append(profit)
                
        max_profit = max(profit_list)
        
        if max_profit > 0:
            return max_profit
        else:
            return 0