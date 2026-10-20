class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        sub=0
        d={}
        i=0
        j=1
        while j<len(nums):
            sub=nums[i]+nums[j]
            d[sub]=d.get(sub,0)+1
            i+=1
            j+=1
        for i,j in d.items():
            if j>1:
                return True
        return False
        