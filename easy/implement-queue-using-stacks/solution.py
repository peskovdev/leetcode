class MyQueue:
    def __init__(self):
        self.stack = []
        self.popstack = []

    def push(self, x: int) -> None:
        while self.popstack:
            self.stack.append(self.popstack.pop())
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.popstack.append(self.stack.pop())
        return self.popstack.pop()
        # return self.popstack.pop() if self.popstack else -1

    def peek(self) -> int:
        while self.stack:
            self.popstack.append(self.stack.pop())
        return self.popstack[-1]
        # return self.popstack[-1] if self.popstack else -1

    def empty(self) -> bool:
        return not (self.stack or self.popstack)
