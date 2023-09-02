from string import ascii_lowercase, ascii_uppercase

alnum_letters = set(f"{ascii_lowercase}{ascii_uppercase}1234567890")


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_up = ""
        for c in s:
            if c in alnum_letters:
                s_up += c.lower()
        return s_up == s_up[::-1]
