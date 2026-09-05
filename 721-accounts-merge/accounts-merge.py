class Disjoint_set:
    def __init__(self,n):
        self.par=list(range(n+1))
        self.rank=[0]*(n+1)
        self.size=[1]*(n+1)
    def find_set(self,node):
        if node==self.par[node]:
            return node
        self.par[node]=self.find_set(self.par[node])
        return self.par[node]
        
    def union_by_size(self,u,v):
        root_u=self.find_set(u)
        root_v=self.find_set(v)
        if root_u==root_v:
            return
        if self.size[root_v]<self.size[root_u]:
            self.par[root_v]=root_u
            self.size[root_u]=self.size[root_u]+self.size[root_v]
        else:
            self.par[root_u]=root_v
            self.size[root_v]=self.size[root_v]+self.size[root_u]
            
    def union_by_rank(self,u,v):
        root_u=self.find_set(u)
        root_v=self.find_set(v)
        if root_u==root_v:
            return
        if self.rank[root_u]<self.rank[root_v]:
            self.par[u]=self.par[v]
        elif self.rank[root_u]>self.rank[root_v]:
            self.par[v]=self.par[u]
        else:
            self.par[v]=self.par[u]
            self.rank[root_u]+=1
            

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        ds=Disjoint_set(n)
        dic={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail=accounts[i][j]
                if mail not in dic:
                    dic[mail]=i
                else:
                    ds.union_by_size(i,dic[mail])

        merged=[[] for _ in range(n)]

        for mail,node in dic.items():
            root=ds.find_set(node)
            merged[root].append(mail)
        
        #create final answer
        ans=[]
        for i in range(n):
            if len(merged[i])==0:
                continue
            merged[i].sort()
            temp=[]
            temp.append(accounts[i][0]) #Name
            temp.extend(merged[i])      # Email
            ans.append(temp)
        return ans




        