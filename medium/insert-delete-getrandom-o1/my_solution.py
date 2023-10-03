import random


class RandomizedSet:
    def __init__(self):
        self.numdict = {}  # {val: index}
        self.numlist = []

    def insert(self, val: int) -> bool:
        if val in self.numdict:
            return False
        self.numlist.append(val)
        self.numdict[val] = len(self.numlist) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numdict:
            return False
        index, last_val = self.numdict[val], self.numlist[-1]
        self.numlist[index] = last_val
        self.numlist.pop()
        self.numdict[last_val] = index
        del self.numdict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.numlist)
