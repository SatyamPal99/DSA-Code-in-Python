from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        
        vis=[0]*numCourses
        pathVis=[0]*numCourses
        for i in range(numCourses):
            if vis[i]==0:
                if self.dfs(adj,vis,pathVis,i):
                    return False
        return True"""

        #using BFS/Topological sort...

        indeg=[0]*numCourses
        q=deque()

        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)

        for i in range(numCourses):
            for j in adj[i]:
                indeg[j]+=1
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)

        count=0
        while q:
            node=q.popleft()
            count+=1
            for i in adj[node]:
                indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
        if count!=numCourses:
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

            

        