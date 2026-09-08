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
            return False
        if self.size[root_v]<self.size[root_u]:
            self.par[root_v]=root_u
            self.size[root_u]=self.size[root_u]+self.size[root_v]
        else:
            self.par[root_u]=root_v
            self.size[root_v]=self.size[root_v]+self.size[root_u]
        return True

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
    def removeStones(self, stones: List[List[int]]) -> int:
        maxRow=0
        maxCol=0
        n=0
        for r,c in stones:
            maxRow=max(maxRow,r)
            maxCol=max(maxCol,c)
            n+=1

        ds=Disjoint_set(maxRow+maxCol+2)
        stoneSet=set()
        for r,c in stones:
            rowNode=r
            colNode=c+maxRow+1
            ds.union_by_size(rowNode,colNode)
            stoneSet.add(rowNode)
            stoneSet.add(colNode)
        
        components=0
        for node in stoneSet:
            if ds.find_set(node)==node:
                components+=1
        
        return n-components

        

        
        