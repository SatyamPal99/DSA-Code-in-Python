class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        """dp=[[None]*(n) for _ in range(n)]
        return self.fun(triangle,0,0,dp)"""

        # Tabular DP...

        """dp=[[None]*n for _ in range(n)]
        for i in range(n):
            dp[n-1][i]=triangle[n-1][i]

        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down=triangle[i][j]+dp[i+1][j]
                dia=triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(down,dia)
        return dp[0][0]"""

        # space optimization...

        prev=[0]*n
        for i in range(n):
            prev[i]=triangle[n-1][i]
        for i in range(n-2,-1,-1):
            curr=[None]*(n)
            for j in range(i,-1,-1):
                down=triangle[i][j]+prev[j]
                dia=triangle[i][j]+prev[j+1]
                curr[j]=min(down,dia)
            prev=curr
        return prev[0]
        


    def fun(self,arr,i,j,dp):
        if i==len(arr)-1:
            return arr[i][j]

        if dp[i][j]!=None:
            return dp[i][j]

        down=arr[i][j]+self.fun(arr,i+1,j,dp)
        dia=arr[i][j]+self.fun(arr,i+1,j+1,dp)

        dp[i][j]=min(down,dia)
        return dp[i][j]
        