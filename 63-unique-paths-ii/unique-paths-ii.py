class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        """dp=[[-1]*m for _ in range(n)]
        return self.fun(n-1,m-1,grid,dp)"""

        # Tabular DP
        """dp=[[0]*(m) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    continue
                elif i==0 and j==0 :
                    if grid[i][j]==1:
                        dp[i][j]=0
                    dp[i][j]=1
                else:
                    up=0
                    left=0
                    if i>0 and grid[i][j]==0:
                        up=dp[i-1][j]
                    if j>0 and grid[i][j]==0:
                        left=dp[i][j-1]
                    dp[i][j]=up+left
        return dp[n-1][m-1]"""

        # space optimization...

        prev=[0]*m
        for i in range(n):
            temp=[0]*m
            for j in range(m):
                if grid[i][j]==1:
                    continue
                elif i==0 and j==0 :
                    if grid[i][j]==1:
                        dp[i][j]=0
                    temp[j]=1
                else:
                    up=0
                    left=0
                    if i>0 and grid[i][j]==0:
                        up=prev[j]
                    if j>0 and grid[i][j]==0:
                        left=temp[j-1]
                    temp[j]=up+left
            prev=temp
        return prev[-1]




    def fun(self,n,m,grid,dp):
        if n<0 or m<0:
            return 0
        if n==0 and m==0:
            if grid[n][m]==1:
                return 0
            return 1
        if n>=0 and m>=0 and grid[n][m]==1:
            return 0

        if dp[n][m]!=-1:
            return dp[n][m]

        up=self.fun(n-1,m,grid,dp)
        left=self.fun(n,m-1,grid,dp)
        dp[n][m]=up+left
        return dp[n][m]
        