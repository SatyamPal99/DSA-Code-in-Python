class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], th: int) -> int:
        
        cost=[[math.inf]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    cost[i][j]=0

        for u,v,wt in edges:
            cost[u][v]=wt
            cost[v][u]=wt
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    cost[i][j]=min(cost[i][j],cost[i][via]+cost[via][j])
        
        cout_max=n+1
        city=-1
        for i in range(n):
            c=0
            for j in range(n):
                if cost[i][j]<=th:
                    c+=1
            if c<=cout_max:
                cout_max=c
                city=i
        return city


        