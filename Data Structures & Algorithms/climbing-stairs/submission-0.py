class Solution:
    def climbStairs(self, n: int) -> int:
        # init status for 1 and 2
        # trans function: f(i) = f(i-1) + f(i-2)
        # return f(n)
        if n<3:
            return n
        dp = [0 for item in range(n+1)]
        dp[1], dp[2] = 1,2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
