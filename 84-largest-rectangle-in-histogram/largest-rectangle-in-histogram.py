class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        LSE=[-1]*n
        RSE=[n]*n
        st1=[]
        for i in range(len(heights)):
            while st1 and heights[st1[-1]]>heights[i]:
                st1.pop()
            if not st1:
                LSE[i]=-1
            else:
                LSE[i]=st1[-1]
            st1.append(i)
        
        st2=[]
        for i in range(len(heights)-1,-1,-1):
            while st2 and heights[st2[-1]]>=heights[i]:
                st2.pop()
            if not st2:
                RSE[i]=n
            else:
                RSE[i]=st2[-1]
            st2.append(i)

        maxi=-9999
        for i in range(len(heights)):
            maxi=max(maxi,heights[i]*(RSE[i]-LSE[i]-1))
        return maxi


        