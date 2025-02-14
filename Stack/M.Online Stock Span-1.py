class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        c = 1
        while self.stack and price >= self.stack[-1][0]:
            [prev_price, prev_c] = self.stack.pop()
            c += prev_c
        self.stack.append([price, c])
        return c
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

""" 
use a monotonicly decreasing stack
pop out those days that are the same or lesser
"""