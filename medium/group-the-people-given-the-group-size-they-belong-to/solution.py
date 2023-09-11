from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        counter = defaultdict(list)
        for i, size in enumerate(groupSizes):
            counter[size].append(i)

        res = []
        for size, people in counter.items():
            for _ in range(len(people) // size):
                group = []
                for i in range(size):
                    group.append(people.pop())
                res.append(group)

        return res
