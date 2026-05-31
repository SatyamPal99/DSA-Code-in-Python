class Solution:
    def searchInsert(self, nums: List[int], tar: int) -> int:
        # Using Binary Search
        """i=0
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
            return mid+1"""

        # Using Lower Bound
        i=0
        j=len(nums)-1
        ans=len(nums)
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]>=tar:
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
        