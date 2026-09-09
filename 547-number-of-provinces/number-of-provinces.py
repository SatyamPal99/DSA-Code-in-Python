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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """v=len(isConnected)
        adj=[[] for _ in range(v)]
        for l in range(v):
            for m in range(v):
                if isConnected[l][m]==1 and l!=m:
                    adj[l].append(m)
                    adj[m].append(l)

        ans=0
        vis=[0]*v
        for i in range(v):
            if vis[i]==0:
                self.bfs(i,vis,adj)
                ans+=1
        return ans

    def bfs(self,i,vis,adj):
        q=deque()
        q.append(i)
        vis[i]=1
        while q:
            temp=q.popleft()
            for k in adj[temp]:
                if vis[k]==0:
                    q.append(k)
                    vis[k]=1"""

        n=len(isConnected)
        ds=Disjoint_set(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    ds.union_by_size(i,j)
                    
        components=0
        for node in range(n):
            if ds.find_set(node)==node:
                components+=1
        return components





   