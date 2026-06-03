class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        i=0
        n=len(nums) 
        j=n-1
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]==tar:
                return mid
            # checking which half is sorted i.e left or right 
            elif nums[mid]>=nums[i]:
                # check if target lies in btw arr[i] and arr[mid]...
                if tar>=nums[i] and tar<=nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
            else:
                if tar<=nums[j] and tar>=nums[mid]:
                    i=mid+1
                else:
                    j=mid-1
        return -1
        