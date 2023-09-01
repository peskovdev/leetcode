from typing import List, DefaultDict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashdict = DefaultDict(list)  # {sorted_str: [str1, str2, str3]}
        for s in strs:
            hashdict[str(sorted(s))].append(s)

        return list(hashdict.values())
