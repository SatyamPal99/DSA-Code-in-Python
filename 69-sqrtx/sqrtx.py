import math
class Solution:
    def mySqrt(self, x: int) -> int:
        #using math library(sqrt(x) give float so use isqrt(x) for int )....
        """return math.isqrt(x)"""


        # Iterative soluiton.... (tc=O(n))
        """ans=0
        for i in range(1,x+1):
            if i*i<=x:
                ans=i
            else:
                break
        return ans"""


        #using binary search....

        low=1
        high=x
        ans=0
        while(low<=high):
            mid=(low+high)//2
            if mid*mid>x:
                high=mid-1
            else:
                ans=mid
                low=mid+1
        return ans
            


        