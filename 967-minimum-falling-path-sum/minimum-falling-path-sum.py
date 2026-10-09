class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        """ans=math.inf
        dp=[[None]*(n) for _ in range(n)]
        for i in range(n-1,-1,-1):
            temp=self.fun(matrix,n-1,i,dp)
            ans=min(ans,temp)
        return ans"""

        """dp=[[None]*(n) for _ in range(n)]
        for i in range(n):
            dp[0][i]=matrix[0][i]

        for i in range(1,n):
            for j in range(0,n):
                left=(math.inf)
                right=(math.inf)
                if j-1>=0:
                    left=matrix[i][j]+dp[i-1][j-1]
                if j+1<n:
                    right=matrix[i][j]+dp[i-1][j+1]
                up=matrix[i][j]+dp[i-1][j]
                dp[i][j]=min(left,right,up)

        mini=math.inf
        for i in range(n):
            mini=min(mini,dp[n-1][i])
        return mini"""

        # Space optimization...
        prev=[0 for _ in range(n)]
        for i in range(n):
            prev[i]=matrix[0][i]
        for i in range(1,n):
            curr=[0 for i in range(n)]
            for j in range(n):
                left=(math.inf)
                right=(math.inf)
                if j-1>=0:
                    left=matrix[i][j]+prev[j-1]
                if j+1<n:
                    right=matrix[i][j]+prev[j+1]
                up=matrix[i][j]+prev[j]
                curr[j]=min(left,right,up)
            prev=curr

        mini=math.inf
        for i in range(n):
            mini= min(mini,prev[i])
        return mini
        


    def fun(self,arr,i,j,dp):
        if j<0 or j>=len(arr):
            return math.inf
        if i==0:
            return arr[0][j]

        if dp[i][j]!=None:
            return dp[i][j]

        left_dia=arr[i][j]+self.fun(arr,i-1,j-1,dp)
        right_dia=arr[i][j]+self.fun(arr,i-1,j+1,dp)
        up=arr[i][j]+self.fun(arr,i-1,j,dp)

        dp[i][j]= min(left_dia,min(right_dia,up))
        return dp[i][j]
        