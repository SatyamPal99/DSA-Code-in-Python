class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """i=0
        j=0
        count=0
        ans=0
        while(j<len(nums)):
            if nums[i]==1 and nums[j]==1:
                count+=1
                j+=1
            else:
                i=j+1
                j+=1
                count=0
            ans=max(ans,count)
        return ans"""

        count=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                maxi=max(maxi,count)
            else:
                count=0
        return maxi

        