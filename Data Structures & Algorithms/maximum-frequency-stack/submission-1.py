class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.frequency = defaultdict(list)
        self.maxCount = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.frequency[self.count[val]].append(val)
        self.maxCount = max(self.maxCount, self.count[val])

    def pop(self) -> int:
        val = self.frequency[self.maxCount].pop()
        self.count[val] -= 1
        if len(self.frequency[self.maxCount]) == 0:
            self.maxCount -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()