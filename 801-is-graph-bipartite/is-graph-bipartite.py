class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V=len(graph)
        vis=[-1]*V
        for i in range(V):
            if vis[i]==-1:
                if self.bfs(graph,vis,i)==False:
                    return False
        return True
    def bfs(self,graph,vis,node):
        q=deque()
        q.append(node)
        vis[node]=0
        while q:
            temp=q.popleft()
            for k in graph[temp]:
                if vis[k]==-1:
                    q.append(k)
                    vis[k]= not vis[temp]
                elif vis[k]==vis[temp]:
                    return False



        