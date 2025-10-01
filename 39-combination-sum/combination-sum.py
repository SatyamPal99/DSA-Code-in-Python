class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        lis=[]
        self.fun(candidates,0,target,ans,lis)
        return ans

    def fun(self,arr,i,tar,ans,lis):
        if i>=len(arr) or tar==0:
            if tar==0:
                ans.append(lis[:])
            return

        if tar>=arr[i]:
            lis.append(arr[i])
            self.fun(arr,i,tar-arr[i],ans,lis)
            lis.pop()
        self.fun(arr,i+1,tar,ans,lis)
        