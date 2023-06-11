class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_base = dict.fromkeys(magazine, 0)
        for char in magazine:
            letter_base[char] += 1

        for char in ransomNote:
            num_of_char = letter_base.get(char)
            if not num_of_char:
                return False
            if num_of_char > 0:
                letter_base[char] -= 1
            else:
                return False
        return True


sol = Solution()
print(sol.canConstruct("a", "b"))
print(sol.canConstruct("aa", "ab"))
print(sol.canConstruct("aa", "aab"))
