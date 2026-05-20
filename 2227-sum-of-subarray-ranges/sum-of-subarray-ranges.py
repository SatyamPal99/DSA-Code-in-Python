class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """total=0
        for i in range(len(nums)):
            small=nums[i]
            lar=nums[i]
            for j in range(i+1,len(nums)):
                small=min(small,nums[j])
                lar=max(lar,nums[j])
                total=total+(lar-small)         
        return total"""

        return self.sumMax(nums)-self.sumMin(nums)

    def sumMin(self,arr):
        n=len(arr)
        small_l=[-1]*len(arr)
        small_r=[n]*n
        st1=[]
        for i in range(len(arr)):
            while st1 and arr[st1[-1]]>arr[i]:
                st1.pop()
            if not st1:
                small_l[i]=-1
            else:
                small_l[i]=st1[-1]
            st1.append(i)
        
        st2=[]
        for i in range(len(arr)-1,-1,-1):
            while st2 and arr[st2[-1]]>=arr[i]:
                st2.pop()
            if not st2:
                small_r[i]=n
            else:
                small_r[i]=st2[-1]
            st2.append(i)
        total=0
        for i in range(len(arr)):
            lmax=i-small_l[i]
            rmax=small_r[i]-i
            total=(total+(lmax*rmax)*arr[i])
        return total



    def sumMax(self,arr):
        n=len(arr)
        small_l=[-1]*len(arr)
        small_r=[n]*n
        st1=[]
        for i in range(len(arr)):
            while st1 and arr[st1[-1]]<arr[i]:
                st1.pop()
            if not st1:
                small_l[i]=-1
            else:
                small_l[i]=st1[-1]
            st1.append(i)
        
        st2=[]
        for i in range(len(arr)-1,-1,-1):
            while st2 and arr[st2[-1]]<=arr[i]:
                st2.pop()
            if not st2:
                small_r[i]=n
            else:
                small_r[i]=st2[-1]
            st2.append(i)
        total=0
        for i in range(len(arr)):
            lmax=i-small_l[i]
            rmax=small_r[i]-i
            total=(total+(lmax*rmax)*arr[i])
        return total


                 
        