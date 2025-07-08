class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        # TC = O(nlogn + 2n)
        ans=[]
        arr.sort()
        for i in range(len(arr)):
            st=arr[i][0]
            end=arr[i][1]
            if(len(ans)!=0 and end<=ans[len(ans)-1][1]):
                continue
            for j in range(i+1,len(arr)):
                if arr[j][0] <= end:
                    end=max(end,arr[j][1])
            ans.append([st,end])
        return ans

        # TC=O(N)
        """ans=[]
        arr.sort()
        for i in range(len(arr)):
            if(len(ans)==0 or arr[i][0]>ans[len(ans)-1][1]):
                st=arr[i][0]
                end=arr[i][1]
                ans.append([st,end])
            else:
                ans[len(ans)-1][1]=max(ans[len(ans)-1][1],arr[i][1])
        return ans"""