class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """V=len(graph)
        vis=[0]*V
        pathVis=[0]*V
        safe=[0]*V
        ans=[]
        for i in range(V):
            if vis[i]==0:
                self.dfs(graph,vis,pathVis,i,safe)
        for i in range(V):
            if safe[i]==1:
                ans.append(i)
        return ans"""

        # using BFS/ toposort...

        V=len(graph)
        indeg=[0]*V
        adj=[[] for _ in range(V)]
        for i in range(V):
            for j in graph[i]:
                adj[j].append(i)
                indeg[i]+=1
        ans=[]
        q=deque()
        for i in range(V):
            if indeg[i]==0:
                q.append(i)
        while(q):
            node=q.popleft()
            ans.append(node)
            for i in adj[node]:
                indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
        ans.sort()
        return ans





        ans=[]



    def dfs(self,adj,vis,pathVis,node,safe):
        vis[node]=1
        pathVis[node]=1
        safe[node]=0
        for i in adj[node]:
            if vis[i]==0:
                if self.dfs(adj,vis,pathVis,i,safe)==True:
                    # if cycle then this is not a safe node...
                    safe[node]=0
                    return True
            elif pathVis[i]==1:
                # if cycle then this is not a safe node...
                safe[node]=0
                return True
        #if there is no cycle then this node is safe node...
        safe[node]=1
        pathVis[node]=0
        return False


        