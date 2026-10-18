class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        """c=0
        for i in range(len(nums)):
            prod=1
            for j in range(i,len(nums)):
                prod=prod*nums[j]
                if prod<k:
                    c+=1
        return c"""

        if len(nums)==1:
            if nums[0]>k:
                return 0
            else:
                return 1


        c=0
        prod=1
        l=0
        r=0
        while r<len(nums):
            prod=prod*nums[r]
            if prod<k:
                c=c+(r-l+1)
            else:
                while prod>=k:
                    if l==r:
                        break
                    prod=prod//nums[l]
                    l+=1
                    if prod<k:
                        c=c+(r-l+1)
            r+=1

        return c


        