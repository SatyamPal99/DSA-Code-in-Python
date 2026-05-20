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
        PS_left=[-1]*len(arr)
        NS_right=[n]*len(arr)
        st1=[]
        for i in range(len(arr)):
            while st1 and arr[st1[-1]]>arr[i]:
                st1.pop()
            if not st1:
                PS_left[i]=-1
            else:
                PS_left[i]=st1[-1]
            st1.append(i)

        st2=[]
        for i in range(len(arr)-1,-1,-1):
            while st2 and arr[st2[-1]]>=arr[i]:
                st2.pop()
            if not st2:
                NS_right[i]=n
            else:
                NS_right[i]=st2[-1]
            st2.append(i)
        total=0 
        for i in range(len(arr)):
            lmax=i-PS_left[i]
            rmax=NS_right[i]-i
            total=(total+(lmax*rmax)*arr[i])%(10**9+7)
        return total
        