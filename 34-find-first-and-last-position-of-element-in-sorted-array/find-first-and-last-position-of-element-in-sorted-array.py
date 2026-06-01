class Solution:
    def searchRange(self, nums: List[int], tar: int) -> List[int]:
        i=0
        n=len(nums)
        j=n-1
        ans=-1
        res=[]
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]<tar:
                i=mid+1
            elif nums[mid]>tar:
                j=mid-1
            else:
                ans=mid
                j=mid-1
        res.append(ans)


        i=0
        j=n-1
        ans1=-1
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]<tar:
                i=mid+1
            elif nums[mid]>tar:
                ans=mid
                j=mid-1
            else:
                ans1=mid
                i=mid+1
        res.append(ans1)
        return res