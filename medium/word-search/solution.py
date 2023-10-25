from collections import Counter, defaultdict


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        path = set()

        def find(i, row, col):
            if i == len(word):
                return True
            if not (
                0 <= row < len(board) and 0 <= col < len(board[0])
                and (row, col) not in path
                and board[row][col] == word[i]
            ):
                return False

            path.add((row, col))
            res = (
                find(i + 1, row + 1, col)
                or find(i + 1, row - 1, col)
                or find(i + 1, row, col + 1)
                or find(i + 1, row, col - 1)
            )
            path.remove((row, col))
            return res

        # Reverse the word if freq of the 1st is greater than freq of the last one
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if find(0, row, col):
                    return True
        return False
