class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """total=0
        for i in range(len(arr)):
            mini=arr[i]
            for j in range(i,len(arr)):
                if arr[j]<mini:
                    mini=arr[j]
                total=total+mini
        return total%(10**9+7)"""


        n=len(arr)
        left_s=[-1]*len(arr)
        right_s=[n]*len(arr)
        st1=[]
        for i in range(len(arr)):
            while st1 and arr[st1[-1]]>arr[i]:
                st1.pop()
            if not st1:
                left_s[i]=-1
            else:
                left_s[i]=st1[-1]
            st1.append(i)

        st2=[]
        for i in range(len(arr)-1,-1,-1):
            while st2 and arr[st2[-1]]>=arr[i]:
                st2.pop()
            if not st2:
                right_s[i]=n
            else:
                right_s[i]=st2[-1]
            st2.append(i)
        total=0 
        for i in range(len(arr)):
            lmax=i-left_s[i]
            rmax=right_s[i]-i
            total=(total+(lmax*rmax)*arr[i])%(10**9+7)
        return total%(10**9+7)
        