class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ds=[]
        i=0
        ans=[]
        nums.sort()
        self.fun(nums,i,ds,ans)
        return ans

    def fun(self,nums,i,ds,ans):
        ans.append(ds.copy())
        for j in range(i, len(nums)):
            if (j!=i and nums[j]==nums[j-1]):
                continue
            ds.append(nums[j])
            self.fun(nums,j+1,ds,ans)
            ds.pop()
        