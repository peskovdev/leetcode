from typing import DefaultDict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashdict: dict = DefaultDict(int)
        for i in s:
            hashdict[i] += 1
        for i in t:
            hashdict[i] -= 1

        for el in hashdict.values():
            if el != 0:
                return False
        return True
