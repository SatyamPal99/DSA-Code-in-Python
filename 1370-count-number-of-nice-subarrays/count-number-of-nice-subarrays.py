class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """return self.fun(nums,k)-self.fun(nums,k-1)"""


        for i in range(len(nums)):
            nums[i] %= 2
        
        prefix_count = [0] * (len(nums) + 1)
        prefix_count[0] = 1
        s = 0
        ans = 0
        
        for num in nums:
            s += num
            if s >= k:
                ans += prefix_count[s - k]
            prefix_count[s] += 1
        
        return ans
        
    def fun(self,nums,k):
        if k<0:
            return 0
        l=0
        r=0
        summ=0
        cout=0
        while r<len(nums):
            summ=summ+(nums[r]%2)
            while summ>k:
                summ=summ-(nums[l]%2)
                l+=1
            cout=cout+(r-l+1)
            r+=1
        return cout
            

        