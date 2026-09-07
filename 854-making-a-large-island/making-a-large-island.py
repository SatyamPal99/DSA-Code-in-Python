class Disjoint_set:
    def __init__(self,n):
        self.par=list(range(n+1))
        self.rank=[0]*(n+1)
        self.size=[1]*(n+1)
    def find_set(self,node):
        if node==self.par[node]:
            return node
        self.par[node]=self.find_set(self.par[node])
        return self.par[node]
        
    def union_by_size(self,u,v):
        root_u=self.find_set(u)
        root_v=self.find_set(v)
        if root_u==root_v:
            return
        if self.size[root_v]<self.size[root_u]:
            self.par[root_v]=root_u
            self.size[root_u]=self.size[root_u]+self.size[root_v]
        else:
            self.par[root_u]=root_v
            self.size[root_v]=self.size[root_v]+self.size[root_u]
            
    def union_by_rank(self,u,v):
        root_u=self.find_set(u)
        root_v=self.find_set(v)
        if root_u==root_v:
            return
        if self.rank[root_u]<self.rank[root_v]:
            self.par[u]=self.par[v]
        elif self.rank[root_u]>self.rank[root_v]:
            self.par[v]=self.par[u]
        else:
            self.par[v]=self.par[u]
            self.rank[root_u]+=1
            

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ds=Disjoint_set(n*m)
        cnt=0
        dr=[1,-1,0,0]
        dc=[0,0,1,-1]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    continue
                currNode=i*m+j
                for nei in range(4):
                    new_r=i+dr[nei]
                    new_c=j+dc[nei]
                    if 0<=new_r<n and 0<=new_c<m and grid[new_r][new_c]==1:
                        neiNode=(new_r*m)+new_c
                        ds.union_by_size(currNode,neiNode)

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    continue
                unique_roots=set()
                for k in range(4):
                    n_r=i+dr[k]
                    n_c=j+dc[k]
                    if 0<=n_r<n and 0<=n_c<m and grid[n_r][n_c]==1:
                        padosi=(n_r*m)+n_c
                        root=ds.find_set(padosi)
                        unique_roots.add(root)
                total=0
                for root in unique_roots:
                    total+=ds.size[root]
        
                cnt=max(cnt,total+1)

        for i in range(n*m):
            cnt=max(cnt,ds.size[ds.find_set(i)])
        return cnt