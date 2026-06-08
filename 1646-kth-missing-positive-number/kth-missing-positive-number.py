class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """if k<arr[0]:
            return k
        for i in range(len(arr)):
            if arr[i]<=k:
                k+=1
        return k"""

        #optimized...
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            missing=arr[mid]-(mid+1)
            if missing>=k:
                high=mid-1
            else:
                low=mid+1
        req=k-(arr[high]-(high+1))
        return arr[high]+req
        