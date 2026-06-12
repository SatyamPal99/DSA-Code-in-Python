class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        """for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==tar:
                    return True
        return False"""

        # Optimized Approach...
        for i in range(len(mat)):
            if mat[i][0]<=tar and mat[i][len(mat[0])-1]>=tar:
                low=0
                high=len(mat[0])-1
                while(low<=high):
                    mid=(low+high)//2
                    if mat[i][mid]==tar:
                        return True
                    elif mat[i][mid]<tar:
                        low=mid+1
                    else:
                        high=mid-1
        return False

        