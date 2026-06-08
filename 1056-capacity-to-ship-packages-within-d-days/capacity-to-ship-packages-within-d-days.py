class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Brute force
        """maxi=max(weights)
        sum_=sum(weights)
        for capacity in range(maxi,sum_+1):
            if self.fun(weights,days,capacity)<=days:
                return capacity
        """

        # Optimized.....
        low=max(weights)
        high=sum(weights)
        ans=0
        while(low<=high):
            mid=(low+high)//2
            temp=self.fun(weights,mid)
            if temp<=days:
                ans=temp
                high=mid-1
            else:
                low=mid+1
        return low


    
    def fun(self,arr,cap):
        day=1
        sum=0
        for i in range(len(arr)):
            if sum+arr[i]<=cap:
                sum=sum+arr[i]
            else:
                day+=1
                sum=arr[i]
        return day