class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """summ=0
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    summ=nums[i]+nums[j]+nums[k]
                    if summ==0:
                        temp=[nums[i],nums[j],nums[k]]
                        temp.sort()
                        if temp not in ans:
                            ans.append(temp)
        return ans"""

        ans=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            summ=0
            l=i+1
            r=len(nums)-1
            tar=-nums[i]
            while(l<r):
                summ=nums[l]+nums[r]
                if summ==tar:
                    temp=[nums[i],nums[l],nums[r]]
                    
                    ans.append(temp)
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while r>l and nums[r]==nums[r+1]:
                        r-=1
                elif summ<tar:
                    l+=1
                else:
                    r-=1
        return ans