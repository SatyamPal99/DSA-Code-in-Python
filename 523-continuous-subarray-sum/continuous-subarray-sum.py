class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """summ=0
        for i in range(len(nums)):
            summ=nums[i]
            for j in range(i+1,len(nums)):
                summ=summ+nums[j]
                if summ%k==0:
                    return True
        return False"""

        #sliding window

        summ=0
        d={0:-1}
        
        for i,num in enumerate(nums):
            summ=summ+num
            if k!=0:
                rem=summ%k
            else:
                rem=summ
            if rem in d:
                if i-d[rem]>=2:
                    return True
            else:
                d[rem]=i
        return False
            
        return False
