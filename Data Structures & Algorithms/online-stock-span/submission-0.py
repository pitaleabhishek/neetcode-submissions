class StockSpanner:

    def __init__(self):
       self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        count = 0
        for elem in reversed(range(len(self.stack))):
            if self.stack[elem] <= price:
                count += 1
            elif price < self.stack[elem]:
                return count
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)