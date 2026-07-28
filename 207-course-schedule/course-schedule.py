class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        
        vis=[0]*numCourses
        pathVis=[0]*numCourses
        for i in range(numCourses):
            if vis[i]==0:
                if self.dfs(adj,vis,pathVis,i):
                    return False
        return True


    def dfs(self,adj,vis,pathVis,node):
        vis[node]=1
        pathVis[node]=1
        for i in adj[node]:
            if vis[i]==0:
                if self.dfs(adj,vis,pathVis,i):
                    return True
            elif pathVis[i]==1:
                return True
        pathVis[node]=0
        return False

            

        