class StockSpanner:

    def __init__(self):
        self.output = []

    def next(self, price: int) -> int:
        ret_out = 1

        if self.output:
            for index in range(len(self.output)-1, -1, -1):
                if price >= self.output[index]:
                    ret_out +=1
                elif price < self.output[index]:
                    break

        

        self.output.append(price)
        print(ret_out)
        return ret_out



x = StockSpanner()

x.next(100)
x.next(80)
x.next(70)
x.next(60)
x.next(85)