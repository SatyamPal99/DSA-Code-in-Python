class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Bruteforce...
        """maxfreq=0
        maxcount=0
        for i in range(len(s)):
            mapp={}
            for j in range(i,len(s)):
                mapp[ord(s[j])-ord('A')]=mapp.get(ord(s[j])-ord('A'),0)+1
                maxfreq=max(maxfreq,mapp[ord(s[j])-ord('A')])
                if (j-i+1)-maxfreq<=k:
                    maxcount=max(maxcount,j-i+1)
                else:
                    break
        return maxcount"""

        # Optimized approach ....

        """l=0
        r=0
        mapp={}
        maxfreq=0
        cout=0
        while r<len(s):
            mapp[ord(s[r])-ord('A')]=mapp.get(ord(s[r])-ord('A'),0)+1
            maxfreq=max(maxfreq,mapp[ord(s[r])-ord('A')])
            if (r-l+1)-maxfreq<=k:
                cout=max(cout,r-l+1)
            else:
                while((r-l+1)-maxfreq>k):
                    mapp[ord(s[l])-ord('A')]-=1
                    l+=1
                    maxfreq=max(mapp.values())
            r+=1
        return cout"""

        # Optimized ...

        l=0
        r=0
        mapp={}
        maxfreq=0
        cout=0
        while r<len(s):
            mapp[ord(s[r])-ord('A')] = mapp.get(ord(s[r])-ord('A'),0)+1
            maxfreq=max(maxfreq,mapp[ord(s[r])-ord('A')])
            if (r-l+1)-maxfreq>k:
                mapp[ord(s[l])-ord('A')]-=1
                l+=1
                maxfreq=max(mapp.values())
            cout=max(cout,r-l+1)
            r+=1
        return cout






                


        