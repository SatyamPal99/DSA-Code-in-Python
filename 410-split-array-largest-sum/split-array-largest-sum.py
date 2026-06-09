class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """low=max(nums)
        high=sum(nums)
        for i in range(low,high+1):
            temp=self.fun(nums,i,k)
            if temp<=k:
                return i"""

        # Optimized...
        low=max(nums)
        high=sum(nums)
        ans=0
        while(low<=high):
            mid=(low+high)//2
            temp=self.fun(nums,mid)
            if temp<=k:
                high=mid-1
                ans=mid
            else:
                low=mid+1
        return ans



            
    def fun(self,nums,pages):
        stud=1
        allocated=0
        for i in range(len(nums)):
            if allocated+nums[i]<=pages:
                allocated+=nums[i]
            else:
                allocated=nums[i]
                stud+=1
        return stud

        