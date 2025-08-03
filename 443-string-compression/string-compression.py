class Solution:
    def compress(self, s: List[str]) -> int:
        idx=0
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
        return idx
            
        

        