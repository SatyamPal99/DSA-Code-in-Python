class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """s=set()
        j=0
        for i in nums:
            if i not in s:
                nums[j]=i
                j+=1
                s.add(i)
        return j"""

        i=0
        j=1
        while(j<len(nums)):
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return i+1

            
