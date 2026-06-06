import math
class Solution:
    def mySqrt(self, x: int) -> int:
        #using math library(sqrt(x) give float so use isqrt(x) for int )....
        """return math.isqrt(x)"""

        ans=0
        for i in range(1,x+1):
            if i*i<=x:
                ans=i
            else:
                break
        return ans
        

        