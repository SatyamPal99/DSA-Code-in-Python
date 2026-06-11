class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxi=-1
        idx=-1
        for i in range(len(mat)):
            count=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    count+=1
            if count>maxi:
                idx=i
                maxi=count
        return idx,maxi