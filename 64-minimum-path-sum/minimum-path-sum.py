class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1]*(m) for _ in range(n)]
        return self.fun(n-1,m-1,grid,dp)

    def fun(self,n,m,grid,dp):
        if n==0 and m==0:
            return grid[0][0]
        if n<0 or m<0:
            return 0

        if dp[n][m]!=-1:
            return dp[n][m]

        up=999999
        left=999999
        if n>0:
            up=self.fun(n-1,m,grid,dp)+grid[n][m]
        if m>0:
            left=self.fun(n,m-1,grid,dp)+grid[n][m]
        dp[n][m]=min(up,left)
        return dp[n][m]
        

        