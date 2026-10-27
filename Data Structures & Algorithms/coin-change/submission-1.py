class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initial status: f(1), f(5), f(10) = 1 others float('inf')
        # tran func = f(n) = min(f(n-1), f(n-5), f(n-10))
        # return f(n)
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            min_amount = float('inf')
            for coin in coins:
                if coin <= i:
                    min_amount = min(min_amount, dp[i-coin])
            dp[i] = min_amount+1 
        return dp[amount] if dp[amount] != float('inf') else -1
