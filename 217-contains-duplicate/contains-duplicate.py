class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if j>1:
                return True
        return False