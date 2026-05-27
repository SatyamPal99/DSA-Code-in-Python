class StockSpanner:

    def __init__(self): #when object created then by default constructor returns None..
        self.st=[]

    def next(self, price: int) -> int:
        """self.prices.append(price)
        i=len(self.prices)-1
        span=0
        while i>=0 and self.prices[i]<=price:
            span+=1
            i-=1
        return span"""


        span=1
        while self.st and self.st[-1][0]<=price:
            ele=self.st.pop()
            span=span+ele[1]
        self.st.append([price,span])
        return span
        