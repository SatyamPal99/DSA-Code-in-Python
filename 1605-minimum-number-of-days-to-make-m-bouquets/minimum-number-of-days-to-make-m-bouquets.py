class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    # Brute force....
        """if m*k>len(bloomDay):
            return -1
        mini=min(bloomDay)
        maxi=max(bloomDay)
        for i in range(mini,maxi+1):
            if self.possible(bloomDay,i,m,k)==1:
                return i
        return -1"""

    # Optimized.....
        if m*k>len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=0
        while(low<=high):
            mid=(low+high)//2
            if self.possible(bloomDay,mid,m,k)==1:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans 


    def possible(self,arr,day,m,k):
        count=0
        ans=0
        for j in range(len(arr)):
            if arr[j]<=day:
                count+=1
            else:
                ans=ans+count//k
                count=0
        ans=ans+count//k
        if ans>=m:
            return 1
        else:
            return 0
            
        