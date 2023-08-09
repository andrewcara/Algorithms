import heapq
class MedianFinder:

    def __init__(self):
        self.sum=0
        self.elements =[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.elements, num)
    def findMedian(self) -> float:
        queueLen = len(self.elements)
        print(self.elements)
        if  queueLen%2 == 0:
            return (self.elements[queueLen//2] + self.elements[(queueLen//2)-1]) /2
        else:
            return (self.elements[queueLen//2])

medianFinder =MedianFinder()
medianFinder.addNum(6)
print(medianFinder.findMedian())
medianFinder.addNum(10)   
print(medianFinder.findMedian())
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(6)
print(medianFinder.findMedian())
medianFinder.addNum(5)

print(medianFinder.findMedian())