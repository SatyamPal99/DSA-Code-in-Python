class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """total=0
        for i in range(len(nums)):
            mapp=set()
            for j in range(i,len(nums)):
                mapp.add(nums[j])
                if len(mapp)==k:
                    total+=1
                elif len(mapp)>k:
                    break
        return total"""

        return self.fun(nums,k)-self.fun(nums,k-1)


    def fun(self,nums,k):
        l=0
        r=0
        mapp={}
        ans=0
        while r<len(nums):
            mapp[nums[r]]=mapp.get(nums[r],0)+1
            while len(mapp)>k:
                mapp[nums[l]]-=1
                if mapp[nums[l]]==0:
                    del mapp[nums[l]]
                l+=1
            ans=ans+(r-l+1)
            r+=1
        return ans
            


        