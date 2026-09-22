class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        """dp=[-1]*(n+1)
        return self.fun(n-1,nums,dp)"""

        #Tabular DP
    
        dp=[-1]*(n+1)

        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        dp[0]=nums[0]
        dp[1]=nums[1]
        dp[2]=dp[0]+nums[2]
        ans=max(dp[2],dp[1])
        for i in range(3,n):
            dp[i]=max(dp[i-2]+nums[i],dp[i-3]+nums[i])
            ans=max(ans,dp[i])
        return ans

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
        