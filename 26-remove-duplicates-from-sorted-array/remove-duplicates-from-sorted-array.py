class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s=set()
        j=0
        for i in nums:
            if i not in s:
                nums[j]=i
                j+=1
                s.add(i)
        return j
            
