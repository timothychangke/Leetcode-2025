class StockSpanner:

    def __init__(self):
        self.s = []
        

    def next(self, price: int) -> int:
        c = 1
        while self.s and self.s[-1][0] <= price:
            c += self.s.pop()[1]
        self.s.append((price, c))
        return c
            

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

""" 
[[],[28],[14],[28],[35],[46],[53],[66],[80],[87],[88]]
s = (28, 1) (14, 1) ()
out = 1 1
create a monotonically decreasing stack
"""