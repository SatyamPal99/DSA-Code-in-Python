import math
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for u,v,wt in flights:
            adj[u].append((v,wt))
        dist=[math.inf]*n
        dist[src]=0
        q=deque()
        q.append((0,src,0))
        while q:
            stops,node,dis=q.popleft()
            for nei,wt in adj[node]:
                if dis+wt<dist[nei] and stops<=k:
                    dist[nei]=dis+wt
                    q.append((stops+1,nei,dis+wt))
        if dist[dst]==math.inf:
            return -1
        return dist[dst]


        