class MinStack:


    """def __init__(self):
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
            return ans[1]"""




    def __init__(self):
        self.st=[]
        self.min=10000000

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.min=val
            
        else:
            if val>self.min:
                self.st.append(val)
            else:
                newval=2*val-self.min
                self.st.append(newval)
                self.min=val
    

    def pop(self) -> None:
        if self.min<self.st[-1]:
            self.st.pop()
        else:
            newval=self.st.pop()
            val=self.min
            self.min=2*val-newval

    def top(self) -> int:
        val=self.min
        newval=self.st[-1]
        if newval<val:
            top=self.min
            return top
        else:
            top=self.st[-1]
            return top
    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()