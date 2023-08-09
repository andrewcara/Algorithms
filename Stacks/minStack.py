class MinStack:

    def __init__(self):
        self.minStack = []
        self.MinDic = {}

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append(val)
            self.MinDic[0] = val
        else:
            self.minStack.append(val)
            currentIndex = len(self.minStack)-1
            if val < self.MinDic[currentIndex-1]:
                self.MinDic[currentIndex] = val
            else:
                self.MinDic[currentIndex] = self.MinDic[currentIndex-1]
    def pop(self) -> None:
        self.minStack.pop()
        self.MinDic.popitem

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        currentIndex = len(self.minStack) -1
        return self.MinDic[currentIndex]