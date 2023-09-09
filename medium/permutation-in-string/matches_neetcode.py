from string import ascii_lowercase


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = dict.fromkeys(ascii_lowercase, 0)
        s2_count = dict.fromkeys(ascii_lowercase, 0)
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1

        matches = 0
        for char in ascii_lowercase:
            if s1_count[char] == s2_count[char]:
                matches += 1

        left, right = 0, len(s1)
        while right < len(s2):
            if matches == 26:
                return True

            s2_count[s2[right]] += 1
            if s2_count[s2[right]] == s1_count[s2[right]]:
                matches += 1
            elif s2_count[s2[right]] == s1_count[s2[right]] + 1:
                matches -= 1

            s2_count[s2[left]] -= 1
            if s2_count[s2[left]] == s1_count[s2[left]]:
                matches += 1
            elif s2_count[s2[left]] == s1_count[s2[left]] - 1:
                matches -= 1

            left += 1
            right += 1

        return matches == 26
