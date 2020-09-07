class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        cur=1
        while self.stack:
            if self.stack[-1][0]>price:
                break
            cur+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,cur))
        return cur
            


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(100))