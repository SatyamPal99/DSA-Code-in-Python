class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """dp=[[-1]*(n+1) for _ in range(m)]
        return self.fun(0,0,m,n,dp)"""

        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[m][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                down=dp[i+1][j]
                right=dp[i][j+1]
                dp[i][j]=down+right
        return dp[0][0]


    def fun(self,i,j,m,n,dp):
        if i==m-1 and j==n-1:
            return 1
        if i>=m or j>=n:
            return 0

        if dp[i][j]!=-1:
            return dp[i][j]

        down=self.fun(i+1,j,m,n,dp)
        right=self.fun(i,j+1,m,n,dp)
        dp[i][j]=down+right
        return dp[i][j]
        