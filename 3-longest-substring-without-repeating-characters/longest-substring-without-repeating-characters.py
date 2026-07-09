class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
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
        return maxlen

        