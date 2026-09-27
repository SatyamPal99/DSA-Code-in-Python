class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1]*m for _ in range(n)]
        
        return self.fun(n-1,m-1,grid,dp)

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
        