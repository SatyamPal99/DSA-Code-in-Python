class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n=len(board)
        m=len(board[0])
        vis=[[0]*m for _ in range(n)]
        drow=[-1,0,0,1]
        dcol=[0,1,-1,0]
        for i in range(m):
            if board[0][i]=='O' and vis[0][i]==0:
                self.dfs(0,i,board,vis,drow,dcol)
            if board[n-1][i]=='O' and vis[n-1][i]==0:
                self.dfs(n-1,i,board,vis,drow,dcol)
        for j in range(n):
            if board[j][0]=='O' and vis[j][0]==0:
                self.dfs(j,0,board,vis,drow,dcol)
            if board[j][m-1]=='O' and vis[j][m-1]==0:
                self.dfs(j,m-1,board,vis,drow,dcol)
        
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and board[i][j]=='O':
                    board[i][j]='X'
        

    def dfs(self,row,col,board,vis,drow,dcol):
        n=len(board)
        m=len(board[0])
        vis[row][col]=1
        for i in range(4):
            nrow=row+drow[i]
            ncol=col+dcol[i]
            if 0<=nrow<n and 0<=ncol<m and board[nrow][ncol]=='O' and vis[nrow][ncol]==0:
                self.dfs(nrow,ncol,board,vis,drow,dcol)
            