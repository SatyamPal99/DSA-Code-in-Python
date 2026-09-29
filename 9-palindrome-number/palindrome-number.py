class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num=str(x)
        first=0
        last=len(num)-1
        while first<=last:
            if num[first]==num[last]:
                first+=1
                last-=1
            else:
                return False
        return True