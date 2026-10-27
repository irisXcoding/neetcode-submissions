class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # init dp[0]=0
        # dp[i]: longest len 
        # trans func: dp[i] = dp[i-m] if dp[i-m]<dp[i] for m in range(1, i-1)
        # return dp[n]
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)