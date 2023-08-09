import math
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distWithIndex = []
        rtnList = []
        
        for i in range(len(points)):
            heapq.heappush(distWithIndex, (((math.sqrt(points[i][0]**2 +points[i][1]**2)), i)))
        
        
        
        for i in range(k):
            print(distWithIndex)
            a = heapq.heappop(distWithIndex)
            rtnList.append(points[a[1]])
            
        return rtnList
    
x = Solution().kClosest([[3,3],[5,-1],[-2,4]], k = 2)

print(x)