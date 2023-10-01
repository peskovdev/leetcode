class MyQueue:
    def __init__(self):
        self.stack = []
        self.popstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.popstack:
            return self.popstack.pop()

        while self.stack:
            self.popstack.append(self.stack.pop())
        return self.popstack.pop()

    def peek(self) -> int:
        if self.popstack:
            return self.popstack[-1]

        while self.stack:
            self.popstack.append(self.stack.pop())
        return self.popstack[-1]

    def empty(self) -> bool:
        return not (self.stack or self.popstack)
