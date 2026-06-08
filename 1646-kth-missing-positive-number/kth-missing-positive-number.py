class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k<arr[0]:
            return k
        for i in range(len(arr)):
            if arr[i]<=k:
                k+=1
        return k
        