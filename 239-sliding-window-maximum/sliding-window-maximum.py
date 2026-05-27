class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans=[]
        """for i in range(0,len(nums)-k+1):
            maxi=nums[i]
            for j in range(i,i+k):
                maxi=max(maxi,nums[j])
            ans.append(maxi)
        return ans"""
        

        ans=[]
        dq=deque()
        for i in range(0,len(nums)):
            if dq and dq[0]<=i-k:
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                ans.append(nums[dq[0]])
        return ans

        