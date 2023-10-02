from collections import deque


class NestedInteger:
    """
    This is the interface that allows for creating nested lists.
    You should not implement it, or speculate about its implementation
    """

    def isInteger(self) -> bool:
        """@return True if this NestedInteger holds a single integer, rather than a nested list."""
        return True

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return 0

    def getList(self) -> list["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return []


class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        def get_list(nl: list[NestedInteger]) -> list[int]:
            res = []
            for ni in nl:
                if ni.isInteger():
                    res.append(ni.getInteger())
                else:
                    res.extend(get_list(ni.getList()))
            return res

        self.q = deque(get_list(nestedList))

    def next(self) -> int:
        return self.q.popleft()

    def hasNext(self) -> bool:
        return bool(self.q)
