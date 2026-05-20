class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total=0
        
        for i in range(len(nums)):
            small=nums[i]
            lar=nums[i]
            for j in range(i+1,len(nums)):
                small=min(small,nums[j])
                lar=max(lar,nums[j])
                

                total=total+(lar-small)
                
        return total
                 
        