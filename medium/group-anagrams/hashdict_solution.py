from typing import Counter, DefaultDict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashdict = DefaultDict(list)  # {tuple_formated_hashdict: [str1, str2, str3]}
        for s in strs:
            hashdict[tuple(sorted(Counter(s).items()))].append(s)

        return list(hashdict.values())
