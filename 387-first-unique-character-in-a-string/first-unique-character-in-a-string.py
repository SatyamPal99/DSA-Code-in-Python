class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in range(len(s)):
            if d[s[j]]==1:
                return j
        return -1
        