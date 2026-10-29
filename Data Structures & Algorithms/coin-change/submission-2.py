class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # init: f(i) = 1 for i in coins and others are float('inf') and f(0)=0
        # trans function: f(n) = min(f(n), f(n-i)+1) for i in coins and i< n
        # reuturn f(amount), or -1 if still inf
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for idx in range(1, amount+1):
            for coin in coins:
                if coin <=idx:
                    dp[idx] = min(dp[idx], dp[idx-coin]+1)
        return dp[amount] if dp[amount]!=float("inf") else -1