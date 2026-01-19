class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        mat=[]
        mat = [['.']*n for _ in range(n)]
        col=0
        left_row=[0]*(n)
        lower_diag=[0]*(2*n-1)
        upper_diag=[0]*(2*n-1)
        self.fun(mat,ans,col,left_row,lower_diag,upper_diag,n)
        print(ans)
        return ans

    def fun(self,mat,ans,col,left_row,lower_diag,upper_diag,n):
        if col==n:
            ans.append(["".join(i) for i in mat])
            return
        
        for row in range(n):
            if left_row[row]==0 and lower_diag[row+col]==0 and upper_diag[n-1 + col - row]==0:
                mat[row][col]='Q'
                left_row[row]=1
                lower_diag[row+col]=1
                upper_diag[n-1 + col - row]=1
                self.fun(mat,ans,col+1,left_row,lower_diag,upper_diag,n)
                mat[row][col]='.'
                left_row[row]=0
                lower_diag[row+col]=0
                upper_diag[n-1 + col - row]=0
