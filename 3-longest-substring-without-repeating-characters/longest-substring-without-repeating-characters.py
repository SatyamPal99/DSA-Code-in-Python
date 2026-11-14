class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """maxlen=0
        mapp=[-1]*256
        l=0
        r=0 
        while(r<len(s)):
            idx=ord(s[r])
            if mapp[idx]>=l:
                l=mapp[idx]+1
            maxlen=max(maxlen,r-l+1)
            mapp[idx]=r
            r+=1
        return maxlen"""

        l=0
        h=0
        ans=0
        d={}
        while(h<len(s)):
            d[s[h]]=d.get(s[h],0)+1 
            while(d[s[h]]>1):
                d[s[l]]-=1
                l+=1
            ans=max(ans,h-l+1)
            h+=1
        return ans
        