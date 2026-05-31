class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        i=0
        j=len(nums)-1
        
        while(i<=j):
            mid= (i+j)//2
            if tar>nums[mid]:
                i=mid+1
            elif tar<nums[mid]:
                j=mid-1
            else:
                return mid
        return -1

        