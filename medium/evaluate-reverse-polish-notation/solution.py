class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numstack: list = []
        operations = {
            "+": lambda x, y: int(x) + int(y),
            "-": lambda x, y: int(x) - int(y),
            "*": lambda x, y: int(x) * int(y),
            "/": lambda x, y: int(int(x) / int(y)),
        }

        for t in tokens:
            if t in operations:
                operation = operations[t]
                right_number = numstack.pop()
                left_number = numstack.pop()
                numstack.append(operation(left_number, right_number))
            else:
                numstack.append(t)

        return int(numstack[-1])
