class Solution:
    def isPalindrome(self, s: str) -> bool:
        """s1=s.lower()
        ans=[]
        for i in range(len(s1)):
            if (s1[i]>='a' and s1[i]<='z') or (s1[i]>='A' and s1[i]<='Z') or (s1[i]>='0' and s1[i]<='9'):
                ans.append(s1[i])
        ans="".join(ans)
        j=0
        k=len(ans)-1
        while(j<=k):
            if ans[j]!=ans[k]:
                return False
            else:
                j+=1
                k-=1
        return True"""

        i=0
        j=len(s)-1
        while(i<j):
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].lower()==s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True
        
        