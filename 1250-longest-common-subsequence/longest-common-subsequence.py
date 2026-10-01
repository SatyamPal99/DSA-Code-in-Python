class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1=len(text1)
        n2=len(text2)
        dp=[[-1]*(n2) for _ in range(n1)]
        return self.fun(text1,text2,0,0,dp)
    
    def fun(self,text1,text2,i,j,dp):
        if i==len(text1):
            return 0
        if j==len(text2):
            return 0
        
        if dp[i][j]!=-1:
            return dp[i][j]

        ans=0
        if text1[i]==text2[j]:
            ans= 1+self.fun(text1,text2,i+1,j+1,dp)
        else:
            ans=max(self.fun(text1,text2,i+1,j,dp),self.fun(text1,text2,i,j+1,dp))
        dp[i][j]=ans
        return dp[i][j] 

        