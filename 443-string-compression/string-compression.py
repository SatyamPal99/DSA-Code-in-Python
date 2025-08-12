class Solution:
    def compress(self, s: List[str]) -> int:
        """idx=0
        i=0 
        while i<len(s):
            c=0
            ch=s[i]
            while(i<len(s) and ch==s[i]):
                c+=1
                i+=1
            s[idx]=ch
            idx+=1
            if c>1:
                temp=str(c)
                for j in temp:
                    s[idx]=j
                    idx+=1
        return idx"""

        idx=0
        i=0
        n=len(s)
        while(i<n):
            j=i+1
            while(j<n and s[i]==s[j]):
                j+=1
            s[idx]=s[i]
            idx+=1
            count=j-i
            if (count>1):
                temp=str(count)
                for k in temp:
                    s[idx]=k
                    idx+=1
            i=j
        return idx
            
        

        