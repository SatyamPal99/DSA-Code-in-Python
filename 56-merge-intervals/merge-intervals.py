class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        ans=[]
        arr.sort()
        for i in range(len(arr)):
            if(len(ans)==0 or arr[i][0]>ans[len(ans)-1][1]):
                st=arr[i][0]
                end=arr[i][1]
                ans.append([st,end])
            else:
                ans[len(ans)-1][1]=max(ans[len(ans)-1][1],arr[i][1])
        return ans