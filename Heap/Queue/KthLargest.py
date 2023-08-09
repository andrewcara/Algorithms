class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        
        self.trackDeque = []
        nums.sort(reverse=True)
        if nums:
            for i in range(k):
                self.trackDeque.append(nums[i])
        
    def add(self, val: int) -> int:
        if not self.trackDeque:
            self.trackDeque.append(val)
        
        if val > self.trackDeque[-1]:
            
            self.trackDeque.pop()
            self.trackDeque.append(val)
            arrayLen = len(self.trackDeque)
            if arrayLen ==1:
                return self.trackDeque[0]
            
            for i in range(arrayLen -1):
                
                if self.trackDeque[arrayLen-i-1] > self.trackDeque[arrayLen-i-2]:
                    currentVal = self.trackDeque[arrayLen-i-2]
                    self.trackDeque[arrayLen-i-2] = self.trackDeque[arrayLen-i-1]
                    self.trackDeque[arrayLen-i-1] = currentVal      
        else:
            return self.trackDeque[-1]
        
        return self.trackDeque[-1]


x = KthLargest(1,[])

print((x.add(10)))
print((x.add(11)))
