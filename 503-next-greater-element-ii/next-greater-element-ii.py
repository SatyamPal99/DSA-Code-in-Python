class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """ans=[-1]*len(nums)
        for i in range(len(nums)):
            found=False
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    ans[i]=nums[j]
                    found=True
                    break
            if not found:   
                for k in range(0,i):
                    if nums[k]>nums[i]:
                        ans[i]=nums[k]
                        break
        return ans"""

        """ans=[-1]*len(nums)
        n=len(nums)
        for i in range(len(nums)):
            for j in range(i+1,n+i):
                idx=j%n
                if nums[i]<nums[idx]:
                    ans[i]=nums[idx]
                    break
        return ans"""


        ans=[-1]*len(nums)
        st=[]
        i=2*len(nums)-1
        while (i>=0):
            while st and st[-1]<=nums[i%len(nums)]:
                st.pop()
            if(i<len(nums)):
                if(not st):
                    ans[i]=-1
                else:
                    ans[i]=st[-1]
            st.append(nums[i%len(nums)])
            i-=1
        return ans