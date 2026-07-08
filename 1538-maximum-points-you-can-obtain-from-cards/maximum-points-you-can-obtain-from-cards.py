class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        left_sum=0
        right_sum=0
        max_sum=0
        
        for i in range(k):
            left_sum=left_sum+cardPoints[i]

        max_sum=left_sum
        right_idx=n-1
        for i in range(k-1,-1,-1):
            left_sum=left_sum-cardPoints[i]
            right_sum=right_sum+cardPoints[right_idx]
            max_sum=max(max_sum,left_sum+right_sum)
            right_idx-=1
        return max_sum