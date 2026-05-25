class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        arr=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        
        for j in range(len(matrix[0])):
            sum=0
            for i in range(len(matrix)):
                if matrix[i][j]=="0":
                    sum=0
                    arr[i][j]=sum
                else:
                    sum=sum+int(matrix[i][j])
                    arr[i][j]=sum
        area=0
        for i in range(len(arr)):
            st=[]
            for j in range(len(arr[0])):
                while st and arr[i][st[-1]]>arr[i][j]: #maintaining ascending order in stack
                    ele=st[-1]
                    st.pop()
                    NSE=j
                    PSE=st[-1] if st else -1
                    area=max(area,arr[i][ele]*(NSE-PSE-1))
                st.append(j)
            while st:
                NSE=len(arr[0])
                ele=st.pop()
                PSE=st[-1] if st else -1
                area=max(area, arr[i][ele]*(NSE-PSE-1))
        return area



        