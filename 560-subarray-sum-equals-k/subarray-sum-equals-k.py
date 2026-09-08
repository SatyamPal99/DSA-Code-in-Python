class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """count=0
        for i in range(len(nums)):
            summ=0
            for j in range(i,len(nums)):
                summ=summ+nums[j]
                if summ==k:
                    count+=1
        return count"""

        d={}
        summ=0
        c=0
        for i in nums:
            summ=summ+i
            if summ==k:
                c+=1
            if summ-k in d:
                c=c+d[summ-k]
            d[summ]=d.get(summ,0)+1
        return c
        
        