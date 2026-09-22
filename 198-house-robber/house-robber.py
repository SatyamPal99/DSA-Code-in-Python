class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        return self.fun(n-1,nums,dp)

    def fun(self,n,nums,dp):
        if n==0:
            return nums[n]
        if n<0:
            return 0

        if dp[n]!=-1:
            return dp[n]

        pick=self.fun(n-2,nums,dp)+nums[n]
        not_pick=self.fun(n-1,nums,dp)+0
        dp[n]=max(pick,not_pick)
        return dp[n]
        