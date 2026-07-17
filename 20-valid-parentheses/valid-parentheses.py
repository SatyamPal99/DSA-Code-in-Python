class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(len(s)):
            if s[i]== '(' or s[i]=='{' or s[i]=='[' :
                st.append(s[i])
            else:
                # for test case: "}]" (i.e only closings) or string starting with closing braces.
                if len(st)==0:
                    return False
                ch=st[-1]
                if (s[i]==')' and ch=='(' or 
                 s[i]==']' and ch=='[' or 
                 s[i]=='}' and ch=='{') :
                    st.pop()
                else:
                    return False
                    
        return len(st)==0
        