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

        """l,r = 1,max(nums)
        ans = 1
        while l <= r:
            m = (l+r)//2
            if (sum([ceil(num/m) for num in nums]) <= threshold):
                ans = m
                r = m - 1
            else:
                l = m + 1  
        return ans"""


    # OR 
        low=1
        high=max(nums)
        ans=math.inf
        while(low<=high):
            mid=(low+high)//2
            if self.sum_of_mid(nums,mid)<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def sum_of_mid(self,nums,val):
        sum=0
        for i in range(len(nums)):
            sum=sum+ceil(nums[i]/val)
        return sum
    


    

    