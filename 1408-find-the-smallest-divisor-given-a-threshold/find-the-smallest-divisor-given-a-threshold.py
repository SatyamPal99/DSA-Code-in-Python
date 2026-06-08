import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Binary Search....
        """maxi=max(nums)
        for i in range(1,maxi+1):
            sum=0
            for j in range(len(nums)):
                sum=sum+math.ceil(nums[j]/i)
            if sum<=threshold:
                return i
        return -1"""

        high=max(nums)
        low=1
        ans=math.inf
        while(low<=high):
            mid=(low+high)//2
            temp=self.possible(nums,mid)
            if temp<=threshold:
                if mid<ans:
                    ans=mid
                    high=mid-1
            elif temp>threshold:
                low=mid+1
        return ans

    

    

    def possible(self,nums,val):
        sum=0
        for i in range(len(nums)):
            sum=sum+math.ceil(nums[i]/val)
        return sum

        