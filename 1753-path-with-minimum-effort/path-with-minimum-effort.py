import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n=len(heights)
        m=len(heights[0])
        dist=[[math.inf]*m for _ in range(n)]
        dist[0][0]=0
        p=[]
        heapq.heappush(p,(0,0,0))
        dr=[0,0,-1,1]
        dc=[-1,1,0,0]
        while p:
            diff,row,col=heapq.heappop(p)
            if row==n-1 and col==m-1:
                return diff
            for i in range(4):
                r=row+dr[i]
                c=col+dc[i]
                if 0<=r<=n-1 and 0<=c<=m-1:
                    new_diff=abs(heights[row][col] - heights[r][c])
                    effort=max(new_diff,diff)
                    if effort<dist[r][c]:
                        dist[r][c]=effort
                        heapq.heappush(p,(effort,r,c))
        return -1


        