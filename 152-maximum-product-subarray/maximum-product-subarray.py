class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        """maxi=-99999
        for i in range(len(arr)):
            temp=1
            for j in range(i,len(arr)):
                temp=temp*arr[j]
                maxi=max(temp,maxi)
        return maxi"""

        maxi1=-9999
        pre=1
        suff=1
        maxi2=-9999
        for i in range(len(arr)):
            if pre==0:
                pre=1
            pre=pre*arr[i]
            maxi1=max(maxi1,pre) 
        for j in range(len(arr)-1,-1,-1):
            if suff==0:
                suff=1
            suff=suff*arr[j]
            maxi2=max(maxi2,suff)
        return max(maxi1,maxi2)

        