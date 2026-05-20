class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total=0
        
        for i in range(len(nums)):
            small=9999
            lar=-9999
            for j in range(i+1,len(nums)):
                if small==9999 and lar==-9999 and nums[i]>=nums[j]:
                    lar=nums[i]
                    small=nums[j]
                    print(lar)
                    print(small)
                elif small==9999 and lar==-9999 and nums[i]<nums[j]:
                    lar=nums[j]
                    small=nums[i]
                else:
                    if (nums[j]>lar):
                        lar=nums[j]
                    elif nums[j]<small:
                        small=nums[j]
                total=total+(lar-small)
                
        return total
                 
        