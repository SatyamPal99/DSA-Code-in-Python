class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        """dp=[[-1]*(m) for _ in range(n)]
        return self.fun(n-1,m-1,grid,dp)"""

        # Tabular dp
        """dp=[[0]*(m) for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    up=math.inf
                    left=math.inf
                    if i>0:
                        up=dp[i-1][j]+grid[i][j]
                    if j>0:
                        left=dp[i][j-1]+grid[i][j]
                    dp[i][j]=min(up,left)
        return dp[n-1][m-1]"""

        # space optimization...
        prev=[math.inf]*(m)
        for i in range(n):
            temp=[0]*(m)
            for j in range(m):
                if i==0 and j==0:
                    temp[j]=grid[0][0]
                else:
                    up=math.inf
                    left=math.inf
                    if i>0:
                        up=prev[j]+grid[i][j]
                    if j>0:
                        left=temp[j-1]+grid[i][j]
                    temp[j]=min(up,left)
            prev=temp
        return prev[-1]





    def fun(self,n,m,grid,dp):
        if n==0 and m==0:
            return grid[0][0]
        if n<0 or m<0:
            return math.inf

        if dp[n][m]!=-1:
            return dp[n][m]

        up=self.fun(n-1,m,grid,dp)+grid[n][m]
        left=self.fun(n,m-1,grid,dp)+grid[n][m]
        dp[n][m]=min(up,left)
        return dp[n][m]
        

        