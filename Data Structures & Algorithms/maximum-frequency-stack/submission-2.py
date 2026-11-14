class FreqStack:

    def __init__(self):
        self.stack = defaultdict(list)
        self.count = defaultdict(int)
        self.maxFrequency = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.stack[self.count[val]].append(val)
        self.maxFrequency = max(self.maxFrequency, self.count[val])

    def pop(self) -> int:
        maxElement = self.stack[self.maxFrequency].pop()
        self.count[maxElement] -= 1
        if len(self.stack[self.maxFrequency]) == 0:
            self.maxFrequency -= 1
        return maxElement


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()