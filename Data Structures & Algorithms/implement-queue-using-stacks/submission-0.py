class MyQueue:

    def __init__(self):
        self.queue = []
        self.popQueue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.popQueue:
            return self.popQueue.pop()
        else:
            self.popQueue = self.queue[::-1]
            self.queue = []
        return self.popQueue.pop()

    def peek(self) -> int:
        return self.popQueue[len(self.popQueue)-1] if self.popQueue else self.queue[0]

    def empty(self) -> bool:
        return True if not self.queue and not self.popQueue else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()