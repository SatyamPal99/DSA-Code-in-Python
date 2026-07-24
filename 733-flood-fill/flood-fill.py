class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        vis=[[] for _ in range(len(image))]
        for i in range(len(image)):
            for j in range(len(image[0])):
                vis[i].append(image[i][j])
        initColor=image[sr][sc]
        newColor=color
        delrow=[0,0,1,-1]
        delcol=[1,-1,0,0]
        self.dfs(image,vis,initColor,newColor,delrow,delcol,sr,sc)
        return vis

    def dfs(self,image,vis,ini,new,delrow,delcol,sr,sc):
        vis[sr][sc]=new
        n=len(image)
        m=len(image[0])
        for i in range(4):
            nrow=sr+delrow[i]
            ncol=sc+delcol[i]
            if 0<=nrow<n and 0<=ncol<m and image[nrow][ncol]==ini and vis[nrow][ncol]!=new:
                self.dfs(image,vis,ini,new,delrow,delcol,nrow,ncol)
            



        