import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.list = [x for x in range(1, 1001)]
        self.heap = heapq.heapify(self.list)
        

    def popSmallest(self) -> int:
        return heapq.heappop(self.list)
        
        

    def addBack(self, num: int) -> None:
        if num in self.list:
            return None
        else:
            heapq.heappush(self.list, num)

x = SmallestInfiniteSet()
print(x.addBack(2))
print(x.popSmallest())
print(x.popSmallest())
print(x.popSmallest())
print(x.addBack(1))
print(x.popSmallest())
print(x.popSmallest())
