class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        ans=math.inf
        dp=[[None]*(n) for _ in range(n)]
        for i in range(n-1,-1,-1):
            temp=self.fun(matrix,n-1,i,dp)
            ans=min(ans,temp)
        return ans

    def fun(self,arr,i,j,dp):
        if j<0 or j>=len(arr):
            return math.inf
        if i==0:
            return arr[0][j]

        if dp[i][j]!=None:
            return dp[i][j]

        left_dia=arr[i][j]+self.fun(arr,i-1,j-1,dp)
        right_dia=arr[i][j]+self.fun(arr,i-1,j+1,dp)
        up=arr[i][j]+self.fun(arr,i-1,j,dp)

        dp[i][j]= min(left_dia,min(right_dia,up))
        return dp[i][j]
        