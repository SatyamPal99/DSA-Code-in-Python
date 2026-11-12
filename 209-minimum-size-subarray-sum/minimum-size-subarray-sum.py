class Solution:
    def minSubArrayLen(self, tar: int, nums: list[int]) -> int:
        """ans=math.inf
        for i in range(len(nums)):
            summ=0
            for j in range(i,len(nums)):
                summ=summ+nums[j]
                if summ>=tar:
                    ans=min(ans,j-i+1)
                    break
        if ans==math.inf:
            return 0
        return ans"""

        #Using Sliding window

        ans=math.inf
        j=0
        summ=0
        for i in range(len(nums)):
            summ=summ+nums[i]
            while(summ>=tar):
                ans=min(ans,i-j+1)
                j+=1
                summ=summ-nums[j-1]
        if ans==math.inf:
            return 0
        return ans
                
            

            



