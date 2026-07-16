class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append([i,j,0])
                    vis[i][j]=1
        time=0
        while q:
            temp=q.popleft()
            r=temp[0]
            c=temp[1]
            t=temp[2]
            time=max(time,t)
            d_row=[1,0,-1,0]
            d_col=[0,-1,0,1]
            for i in range(4):
                row=r+d_row[i]
                col=c+d_col[i]
                if row<n and col<m and row>=0 and col>=0 and vis[row][col]==0 and grid[row][col]==1:
                    q.append([row,col,t+1])
                    vis[row][col]=1
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and grid[i][j]==1:
                    return -1
        return time


            

        