class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        i=0
        ans=[]
        lis=[]
        self.fun(nums,i,ans,lis)
        return ans
    def fun(self,nums,i,ans,lis):
        if i==len(nums):
            ans.append(lis[:])
            return
        lis.append(nums[i])
        self.fun(nums,i+1,ans,lis)
        lis.pop()
        self.fun(nums,i+1,ans,lis)

        