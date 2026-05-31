class Solution:
    def searchInsert(self, nums: List[int], tar: int) -> int:
        if len(nums)==1:
            if nums[0]>=tar:
                return 0
            elif nums[0]<tar:
                return 1
        i=0
        j=len(nums)-1
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]<tar:
                i=mid+1
            elif nums[mid]>tar:
                j=mid-1
            else:
                return mid
        if nums[mid]>tar:
            return mid
        elif nums[mid]<tar:
            return mid+1
        