class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]: max rob income ending at i
        # trans func(rob or not): dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        # base case: dp[1]=nums[1] dp[2]=max(nums[1], nums[2])
        # return dp[n-1] n=len(nums)
        # complexity: time: O(n) space: O(n)
        n=len(nums)
        if n==1:
            return nums[0]
        dp = [0]*n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2,  n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[n-1]