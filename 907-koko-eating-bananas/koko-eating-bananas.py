import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #optimized Approach...
        low=1
        high=max(piles)
        ans=math.inf
        while(low<=high):
            mid=(low+high)//2
            tothours=self.fun(piles,mid)
            if tothours<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def fun(self,arr,perhour):
        ans=0
        for i in range(len(arr)):
            temp=math.ceil(arr[i]/perhour)
            ans=ans+temp
        return ans        
        
        