class Solution:
    def countPrimes(self, n: int) -> int:
        """count=0
        for i in range(2,n):
            if(self.isPrime(i)):
                count+=1
        return count"""

        # using seive of eratosthenis
        if n<2:
            return 0
        count=0
        prime=[1]*(n+1)
        prime[0]=0
        prime[1]=0
        for i in range(2,n):
            if prime[i]==1:
                count+=1
                j=i*2
                while j<n:
                    prime[j]=0
                    j+=i
        return count        


    def isPrime(self,n):
        if n<2:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True


