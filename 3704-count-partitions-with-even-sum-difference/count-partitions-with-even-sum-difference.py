class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        l_sum=0
        c=0
        for i in range(len(nums)-1):
            l_sum=l_sum+nums[i]
            r_sum=0
            for j in range(i+1,len(nums)):
                r_sum+=nums[j]
            if abs(l_sum-r_sum)%2==0:
                c+=1
        return c
        