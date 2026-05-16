class MinStack:

    def __init__(self):
        self.st=[]
        

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append([val,val])
        else:
            currmin=self.st[-1]
            self.st.append([val,min(val,currmin[1])])

    def pop(self) -> None:
        if self.st:
            return self.st.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1][0]

    def getMin(self) -> int:
        if self.st:
            ans=self.st[-1]
            return ans[1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()