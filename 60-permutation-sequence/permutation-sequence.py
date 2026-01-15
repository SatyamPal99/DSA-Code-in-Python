class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr=[]
        fact=1
        for i in range(1,n):
            fact=fact*i
            arr.append(i)
        arr.append(n)
        ans=""
        k=k-1
        while(True):
            ans=ans+str(arr[k//fact])
            arr.pop(k//fact)
            if(len(arr)==0):
                break
            k=k%fact
            fact=fact//len(arr)
        return ans


        
        
        
        """arr=[]
        for i in range(1,n+1):
            arr.append(i)
        ans=[]
        idx=0
        self.fun(arr,ans,idx)
        ans.sort()
        temp=ans[k-1]
        return "".join(map(str,temp))

    def fun(self,arr,ans,idx):
        if idx>=len(arr):
            ans.append(arr.copy())
            return
        for i in range(idx,len(arr)):
            arr[i],arr[idx]=arr[idx],arr[i]
            self.fun(arr,ans,idx+1)
            arr[i],arr[idx]=arr[idx],arr[i]"""

        

        