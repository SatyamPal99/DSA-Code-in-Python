class Solution:
    def trap(self, height: List[int]) -> int:
        """total=0        
        for i in range(len(height)):
            lmax=self.leftmax(i,height)
            rmax=self.rightmax(i,height)
            if height[i]<lmax and height[i]<rmax:
                total=total+min(lmax,rmax)-height[i]
        return total
    
    def leftmax(self,l,arr):
        maxi=-9999
        for i in range(l,-1,-1):
            if arr[i]>maxi:
                maxi=arr[i]
        return maxi
    def rightmax(self,i,arr):
        maxi=-9999
        for i in range(i,len(arr)):
            if arr[i]>maxi:
                maxi=arr[i]
        return maxi"""


        prefix=[0]*len(height)
        prefix[0]=height[0]
        for i in range(1,len(height)):
            prefix[i]=max(prefix[i-1],height[i])

        
        suffix=[0]*len(height)
        n=len(height)
        suffix[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            suffix[i]=max(suffix[i+1],height[i])


        total=0        
        for i in range(len(height)):
            lmax=prefix[i]
            rmax=suffix[i]
            if height[i]<lmax and height[i]<rmax:
                total=total+min(lmax,rmax)-height[i]
        return total

    
