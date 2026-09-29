class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        """dp=[-1]*(n+1)
        return self.fun(n-1,nums,dp)"""

        #Tabular DP
        """if n==1:
            return nums[0]
        dp=[-1]*(n+1)
        dp[0]=nums[0]
        dp[1]=nums[1]
        ans=max(dp[0],dp[1])
        for i in range(2,n):
            if i==2:
                dp[i]=dp[i-2]+nums[i]
            else:
                dp[i]=max(dp[i-2]+nums[i],dp[i-3]+nums[i])
            ans=max(dp[i],ans)
        return ans"""



        #Space Optimization...
        if n==1:
            return nums[0]
        prev=nums[1]
        prev1=nums[0]
        prev2=None
        ans=max(prev,prev1)
        for i in range(2,n):
            if i==2:
                curr=prev1+nums[i]
                prev2=prev1
                prev1=prev
                prev=curr
            else:
                curr=max(prev2+nums[i],prev1+nums[i])
                prev2=prev1
                prev1=prev
                prev=curr
            ans=max(ans,curr)
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
        