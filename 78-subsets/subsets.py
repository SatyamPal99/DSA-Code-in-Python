class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        res=[]
        return self.fun(nums,ans,0,res)
        
        
        

    def fun(self,nums,ans,i,res):
        if i==len(nums):
            res.append(ans.copy())
            return res
        ans.append(nums[i])
        left=self.fun(nums,ans,i+1,res)
        ans.pop()
        right=self.fun(nums,ans,i+1,res)
        return res
        
        
        