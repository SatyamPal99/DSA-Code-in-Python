class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """ans=[]
        for i in range(0,len(nums)):
            if len(ans)==0 or ans[0]!=nums[i]:
                cout=0
                for j in range(0,len(nums)):
                    if nums[i]==nums[j]:
                        cout+=1
                if cout>(len(nums)//3):
                    ans.append(nums[i])
            if len(ans)>=2:
                break
        return ans"""

    #Using Hashmap
        d={}
        ans=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i,j in d.items():
            if j>(len(nums)//(3)):
                ans.append(i)
        return ans
    #Moore voting Machine
        ans=[]
        c1=0
        c2=0
        ele1=-1
        ele2=-1
        for i in range(len(nums)):
            if c1==0:
                c1=1
                ele1=nums[i]
            elif c2==0:
                c2=1
                ele2=nums[i]
            elif c1!=0 and nums[i]==ele1:
                c1+=1
            elif c2!=0 and nums[i]==ele2:
                c2+=1
            else:
                c1-=1
                c2-=1
        temp1=0
        temp2=0
        for i in range(len(nums)):
            if nums[i]==ele1:
                temp1+=1
            elif nums[i]==ele2:
                temp2+=1
        n=len(nums)
        if temp1>(n//3):
            ans.append(temp1)
        if temp2>(n//3):
            ans.append(temp2)
        return ans







        