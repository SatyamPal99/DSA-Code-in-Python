class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Bruite force

        # when only input array have 1 element...
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            # if 0th element... 
            if i==0:
                if nums[i]!=nums[i+1]:
                    return nums[i]
            # if last element....
            elif i==len(nums)-1:
                if nums[i]!=nums[i-1]:
                    return nums[i]
            # for not first and not last element...
            else:
                if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                    return nums[i]
        
        #Optimized Code....
        n=len(nums)
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        low=0
        high=n-2
        while(low<=high):
            mid=(low+high)//2
            if mid%2!=0 and nums[mid-1]==nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return nums[mid]

