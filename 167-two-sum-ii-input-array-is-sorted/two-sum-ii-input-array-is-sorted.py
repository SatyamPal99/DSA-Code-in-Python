class Solution:
    def twoSum(self, num: list[int], tar: int) -> list[int]:
        n=len(num)
        i=0
        j=n-1
        summ=0
        while i<j:
            summ=num[i]+num[j]
            if summ==tar:
                return [i+1,j+1]
            elif summ>tar:
                j-=1
            else:
                i+=1
        


        