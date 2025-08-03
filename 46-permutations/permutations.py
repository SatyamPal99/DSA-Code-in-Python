class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        idx=0
        ans=[]
        self.fun(nums,ans,idx)
        return ans
    def fun(self,nums,ans,idx):
        if idx>=len(nums):
            ans.append(nums[:])
            return
        for i in range(idx,len(nums)):
            nums[idx],nums[i]=nums[i],nums[idx]
            self.fun(nums,ans,idx+1)
            nums[idx],nums[i]=nums[i],nums[idx]
