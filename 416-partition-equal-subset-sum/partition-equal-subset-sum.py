class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
        if sum%2!=0:
            return False
        n=len(nums)
        sum=sum//2
        dp=[[None]*(sum+1) for _ in range(n)]
        """return self.fun(nums,sum,len(nums)-1,dp)"""

        # Memoization...
        for i in range(n):
            dp[i][0]=True
        for i in range(1,sum+1):
            if nums[0]==i:
                dp[0][i]=True
            else:
                dp[0][i]=False

        for i in range(1,n):
            for j in range(1,sum+1):
                right=dp[i-1][j]
                left=False
                if nums[i]<=sum:
                    left=dp[i-1][j-nums[i]]
                dp[i][j]=right or left
        return dp[n-1][sum]


    def fun(self,nums,sum,i,dp):
        if sum==0 or nums[i]==sum:
            return True
        if i==0:
            return nums[i]==sum
        
        if dp[i][sum]!=None:
            return dp[i][sum]
            
        right=self.fun(nums,sum,i-1,dp)
        left=False
        if nums[i]<=sum:
            left=self.fun(nums,sum-nums[i],i-1,dp)
        dp[i][sum]=right or left
        return dp[i][sum]
        