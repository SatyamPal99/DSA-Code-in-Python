class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in range(len(num)):
            while st and k>0 and st[-1]>num[i]:
                st.pop()
                k-=1
            st.append(num[i])
        while k>0:
            st.pop()
            k-=1
        if len(st)==0:
            return '0'
        res=[]
        while st:
            ele=st.pop()
            res.append(ele)
        
        while res and res[-1]=='0' and len(res)>1:
            res.pop()
        res=res[::-1]
        if len(res)==0:
            return '0'
            
        
        return "".join(res)
         
        