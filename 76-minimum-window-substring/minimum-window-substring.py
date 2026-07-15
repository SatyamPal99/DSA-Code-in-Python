class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """maxlen=math.inf
        idx=-1
        for i in range(len(s)):
            cout=0
            mapp=[0]*256
            for ch in t:
                mapp[ord(ch)]+=1
            for j in range(i,len(s)):
                if mapp[ord(s[j])]>0:
                    cout+=1
                mapp[ord(s[j])]-=1
                if cout==len(t):
                    if j-i+1<maxlen:
                        maxlen=j-i+1
                        idx=i
                    break
        if idx==-1:
            return ""
        return s[idx:idx+maxlen]"""

        n=len(s)
        m=len(t)
        mapp=[0]*256
        r=0
        l=0
        minlen=math.inf
        idx=-1
        cout=0
        for ch in t:
            mapp[ord(ch)]+=1
        while(r<n):
            if mapp[ord(s[r])]>0:
                cout+=1
            mapp[ord(s[r])]-=1
            while cout==m:
                if r-l+1<minlen:
                    minlen=r-l+1
                    idx=l
                mapp[ord(s[l])]+=1
                if mapp[ord(s[l])]>0:
                    cout-=1
                l+=1
            r+=1
        if idx==-1:
            return ""
        return s[idx:idx+minlen]





        