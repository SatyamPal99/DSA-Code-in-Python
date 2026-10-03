class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        dp=[[None]*(n) for _ in range(n)]
        return self.fun(triangle,0,0,dp)

    def fun(self,arr,i,j,dp):
        if i==len(arr)-1:
            return arr[i][j]

        if dp[i][j]!=None:
            return dp[i][j]

        down=arr[i][j]+self.fun(arr,i+1,j,dp)
        dia=arr[i][j]+self.fun(arr,i+1,j+1,dp)

        dp[i][j]=min(down,dia)
        return dp[i][j]
        