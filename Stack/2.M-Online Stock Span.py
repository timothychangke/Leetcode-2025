class StockSpanner:

    def __init__(self):
        stack = []

    def next(self, price: int) -> int:
        c = 1
        while self.stack and self.stack[0] < price:
            _, count = self.stack.pop()
            c += count
        self.stack.append([price, c])
        return c
            
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)