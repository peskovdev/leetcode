from string import ascii_lowercase


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = dict.fromkeys(ascii_lowercase, 0)
        s2_count = dict.fromkeys(ascii_lowercase, 0)
        matches = 26
        for c in s1:
            if s1_count[c] == s2_count[c]:
                s1_count[c] += 1
                if s1_count[c] != s2_count[c]:
                    matches -= 1
            else:
                s1_count[c] += 1

        left, right = 0, 0
        while right < len(s2):
            s2_count[s2[right]] += 1
            if s2_count[s2[right]] == s1_count[s2[right]]:
                matches += 1
            elif s2_count[s2[right]] == s1_count[s2[right]] + 1:
                matches -= 1

            if matches == 26:
                return True

            if right >= len(s1) - 1:
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == s1_count[s2[left]]:
                    matches += 1
                elif s2_count[s2[left]] == s1_count[s2[left]] - 1:
                    matches -= 1
                left += 1
            right += 1

        return False
