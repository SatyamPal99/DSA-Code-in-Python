class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """idx=0
        ans=[]
        self.fun(nums,ans,idx)
        return ans"""
        ds=[]
        ans=[]
        idx=0
        mp=[0]*len(nums)
        self.fun1(nums,ds,ans,mp)
        return ans

    def fun1(self,nums,ds,ans,mp):
        if len(ds)==len(nums):
            ans.append(ds.copy())
            return
        for i in range(len(nums)):
            if mp[i]==0:
                ds.append(nums[i])
                mp[i]=1
                self.fun1(nums,ds,ans,mp)
                mp[i]=0
                ds.pop()
            




    """def fun(self,nums,ans,idx):
        if idx>=len(nums):
            ans.append(nums[:])
            return
        for i in range(idx,len(nums)):
            nums[idx],nums[i]=nums[i],nums[idx]
            self.fun(nums,ans,idx+1)
            nums[idx],nums[i]=nums[i],nums[idx]"""

        
