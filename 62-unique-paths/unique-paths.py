class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """dp=[[-1]*(n+1) for _ in range(m)]
        return self.fun(0,0,m,n,dp)"""

        # Tabular DP...
        """dp=[[0]*(n+1) for _ in range(m+1)]
        dp[m][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                down=dp[i+1][j]
                right=dp[i][j+1]
                dp[i][j]=down+right
        return dp[0][0]"""

        # Space Optimization
        #top down tabular

        dp=[[0]*(n) for _ in range(m+1)]
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    dp[i][i]=1
                else:
                    up=0
                    down=0
                    if i>0:
                        up=dp[i-1][j]
                    if j>0:
                        down=dp[i][j-1]
                    dp[i][j]=up+down
        return dp[m-1][n-1] 

        """down=1
        right=0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                curr=down+right"""



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
        