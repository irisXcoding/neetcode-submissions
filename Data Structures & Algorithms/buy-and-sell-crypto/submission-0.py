class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = [0 for item in prices]
        best_profit = 0
        for idx, item in enumerate(prices):
            if idx ==0:
                best_buy[0] = prices[0]
                continue
            best_buy[idx] = min(best_buy[idx-1], prices[idx])
        for idx in range(len(prices)):
            if prices[idx]-best_buy[idx]>best_profit:
                best_profit = prices[idx]-best_buy[idx]
        return best_profit





        