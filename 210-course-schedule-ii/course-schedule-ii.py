class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(numCourses)]
        indeg=[0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
        for i in range(numCourses):
            for j in adj[i]:
                indeg[j]+=1
        q=deque()
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        ans=[]
        count=0
        while(q):
            temp=q.popleft()
            ans.append(temp)
            count+=1
            for i in adj[temp]:
                indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
        if count!=numCourses:
            return []
        return ans

        