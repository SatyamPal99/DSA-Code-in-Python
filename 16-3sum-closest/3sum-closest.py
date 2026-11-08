class Solution:
    def threeSumClosest(self, nums: list[int], tar: int) -> int:
        """ans=math.inf
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    summ=nums[i]+nums[j]+nums[k]
                    temp=abs(tar-summ)
                    if temp<ans:
                        ans=temp
                        res=summ
        return res"""

        # using two pointers
        nums.sort()
        ans=math.inf
        res=0
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while(l<r):
                summ=nums[i]+nums[l]+nums[r]
                diff=abs(summ-tar)
                if diff<ans:
                    ans=diff
                    res=summ
                if summ==tar:
                    l+=1
                    r-=1
                elif summ<tar:
                    l+=1
                else:
                    r-=1
        return res

        