class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """maxx=0
        n=len(s)
        for i in range(len(s)):
            mapp={}
            for j in range(i,len(s)):
                mapp[ord(s[j])-ord('a')]=1
                if (mapp.get(0,0)+mapp.get(1,0)+mapp.get(2,0)==3):
                    maxx=maxx+(n-j)
                    break
        return maxx"""

        count=0
        mapp={0:-1,1:-1,2:-1}
        for i in range(len(s)):
            mapp[ord(s[i])-ord('a')]=i
            if mapp.get(0,-1)!=-1 and mapp.get(1,-1)!=-1 and mapp.get(2,-1)!=-1:
                count=count+(min(mapp.get(0,0),mapp.get(1,0),mapp.get(2,0))+1)
        return count




