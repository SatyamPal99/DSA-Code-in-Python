class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """ans=set()
        lis=[]
        i=0
        candidates.sort()
        self.fun(candidates,target,i,ans,lis)
        return list(ans)
    def fun(self,arr,tar,i,ans,lis):
        if i==len(arr) or tar==0:
            if tar==0:
                ans.add(tuple(lis[:]))
            return 
        if tar>=arr[i]:
            lis.append(arr[i])
            self.fun(arr,tar-arr[i],i+1,ans,lis) 
            lis.pop()
        self.fun(arr,tar,i+1,ans,lis)"""

        candidates.sort()
        ans=[]
        ds=[]
        self.fun(0,target,candidates,ans,ds)
        return ans

    def fun(self,i,tar,arr,ans,ds):
        if tar==0:
            ans.append(ds[:])
        for j in range(i,len(arr)):
            if j>i and arr[j]==arr[j-1]:
                continue
            if arr[j]>tar:
                break
            ds.append(arr[j])
            self.fun(j+1,tar-arr[j],arr,ans,ds)
            ds.pop()

        