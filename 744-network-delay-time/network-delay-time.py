import math
from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        vis=[math.inf]*(n+1)
        vis[k]=0
        q=PriorityQueue()
        q.put((0,k))
        while not q.empty():
            dis,node=q.get()
            if dis>vis[node]:
                continue
            for nei,d in adj[node]:
                if dis+d<vis[nei]:
                    vis[nei]=dis+d
                    q.put((dis+d,nei))
            
        ans=max(vis[1:])
        if ans==math.inf:
            return -1
        return ans
        