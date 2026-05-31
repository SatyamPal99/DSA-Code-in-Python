class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        #Iterative 
        """i=0
        j=len(nums)-1
        
        while(i<=j):
            mid= (i+j)//2
            if tar>nums[mid]:
                i=mid+1
            elif tar<nums[mid]:
                j=mid-1
            else:
                return mid
        return -1"""

        #Recursive code
        i=0
        j=len(nums)-1
        return self.fun(nums,i,j,tar)

    def fun(self,arr,i,j,tar):
        mid=(i+j)//2
        if i>j:
            return -1
        elif arr[mid]==tar:
            return mid
        
        if tar>arr[mid]:
            return self.fun(arr,mid+1,j,tar)
        else:
            return self.fun(arr,i,mid-1,tar)


        