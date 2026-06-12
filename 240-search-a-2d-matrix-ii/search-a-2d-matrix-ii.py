class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        j=0
        i=len(mat[0])-1
        while i>=0 and j<len(mat):
            if mat[j][i]>tar:
                i=i-1
            elif mat[j][i]<tar:
                j+=1
            else:
                return True
        return False
        