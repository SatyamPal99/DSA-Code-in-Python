class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==tar:
                    return True
        return False

        