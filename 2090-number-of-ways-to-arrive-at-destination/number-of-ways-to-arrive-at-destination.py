import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=10**9+7
        adj=[[] for _ in range(n)]
        for u,v,wt in roads:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
    
        pq=[]
        dist=[math.inf]*n
        ways=[0]*n
        heapq.heappush(pq,(0,0)) # dis,node
        dist[0]=0
        ways[0]=1
        while pq:
            dis,node=heapq.heappop(pq)
            if dis>dist[node]:
                continue
            for nei,wt in adj[node]:
                new_dis=dis+wt
                if new_dis<dist[nei] :
                    dist[nei]=new_dis
                    ways[nei]=ways[node]
                    heapq.heappush(pq,(new_dis,nei))
                elif new_dis == dist[nei]:
                    ways[nei]=(ways[nei]+ways[node]) % mod
        return ways[n-1]
                



        