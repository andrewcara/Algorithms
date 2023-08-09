import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [i * (-1) for i in stones]
        heapq.heapify(stones)
        
        while len(stones) > 2:
            print(stones)
            a = heapq.heappop(stones) * -1
            b = heapq.heappop(stones) * -1

            if a-b ==0:
                continue
            else:
                heapq.heappush(stones, (a-b) *-1)
        if stones:
            return stones[0] * (-1)
        else:
            return 0
