from copy import deepcopy


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        store: set[str] = set()
        stack: list[list] = [[] for _ in range(n)]

        def backtrack(stack: list[list]) -> None:
            for i in range(len(stack) - 1, 0, -1):
                if len(stack) > 1:
                    new_stack = deepcopy(stack[:i]) + deepcopy(stack[i + 1:])
                    new_stack[i - 1].append(stack[i])
                    backtrack(new_stack)
            combination = (
                str(stack)
                .replace(" ", "")
                .replace(",", "")
                .replace("[", "(")
                .replace("]", ")")
            )[1:-1]
            store.add(combination)

        backtrack(stack)
        return store  # type: ignore
