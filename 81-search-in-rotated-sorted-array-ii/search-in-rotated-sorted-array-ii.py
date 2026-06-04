class Solution:
    def search(self, nums: List[int], tar: int) -> bool:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==tar:
                return True
            elif nums[low]==nums[high]==nums[mid]:
                low=low+1
                high-=1
                continue
            elif nums[low]<=nums[mid]:
                if tar>=nums[low] and nums[mid]>=tar:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if tar>=nums[mid] and tar<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False
        