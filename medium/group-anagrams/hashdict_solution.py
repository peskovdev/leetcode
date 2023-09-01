from typing import DefaultDict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = DefaultDict(list)  # {list_counter: [str1, str2, str3]}
        for s in strs:
            counter = [0] * 26  # a ... z
            for char in s:
                counter[ord(char) - ord("a")] += 1

            res[tuple(counter)].append(s)

        return list(res.values())
