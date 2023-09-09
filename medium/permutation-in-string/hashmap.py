from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count: dict[str, int] = Counter(s1)
        hashchar: dict[str, int] = {}

        left, right = 0, 0
        while right < len(s2):
            hashchar[s2[right]] = 1 + hashchar.get(s2[right], 0)
            if count == hashchar:
                return True

            if right >= len(s1) - 1:
                if hashchar[s2[left]] == 1:
                    del hashchar[s2[left]]
                else:
                    hashchar[s2[left]] -= 1
                left += 1
            right += 1

        return False
