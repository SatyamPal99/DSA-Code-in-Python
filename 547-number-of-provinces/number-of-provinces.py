class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        v=len(isConnected)
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
                self.bfs(isConnected,i,vis,adj)
                ans+=1
        return ans

    def bfs(self,mat,i,vis,adj):
        q=deque()
        q.append(i)
        vis[i]=1
        while q:
            temp=q.popleft()
            for k in adj[temp]:
                if vis[k]==0:
                    q.append(k)
                    vis[k]=1
                    
                





        