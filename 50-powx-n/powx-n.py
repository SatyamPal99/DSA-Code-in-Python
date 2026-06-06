class Solution:
    def myPow(self, x: float, n: int) -> float:
        """return x**n"""

        # Iterative solution
        """if n<0:
            x=1/x
            n=-n
        ans=1
        for i in range(1,n+1):
            ans=ans*x
        return ans"""

        # Optimized Approach...

        if n<0:
            x=1/x
            n=-n
        ans=1
        while(n>0):
            if n%2==1:
                ans=ans*x
                n=n-1
            else:
                x=x*x
                n=n//2

        return ans

        