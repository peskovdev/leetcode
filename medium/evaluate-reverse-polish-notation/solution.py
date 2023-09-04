class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numstack: list = []
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }

        for t in tokens:
            if t in operations:
                operation = operations[t]
                b, a = numstack.pop(), numstack.pop()
                numstack.append(operation(a, b))
            else:
                numstack.append(int(t))

        return numstack[-1]
