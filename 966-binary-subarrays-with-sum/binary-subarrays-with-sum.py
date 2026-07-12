class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """cout=0
        for i in range(len(nums)):
            summ=0
            for j in range(i,len(nums)):
                summ=summ+nums[j]
                if summ==goal:
                    cout+=1
        return cout"""

        # better ...
        return self.fun(nums,goal)-self.fun(nums,goal-1)
        

    def fun(self,nums,goal):
        if goal<0:
            return 0
        l=0
        r=0
        summ=0
        cout=0
        while(r<len(nums)):
            summ=summ+nums[r]
            while summ>goal:
                summ=summ-nums[l]
                l+=1
            cout=cout+(r-l+1)
            r+=1
        return cout