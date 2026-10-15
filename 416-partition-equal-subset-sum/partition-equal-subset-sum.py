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
        return self.fun(nums,sum,len(nums)-1,dp)

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
        