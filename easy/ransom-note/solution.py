class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_base = list(magazine)
        for char in ransomNote:
            if char not in letter_base:
                return False
            letter_base.pop(letter_base.index(char))
        return True


sol = Solution()
print(sol.canConstruct("a", "b"))
print(sol.canConstruct("aa", "ab"))
print(sol.canConstruct("aa", "aab"))
