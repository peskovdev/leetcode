class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_up = ""
        for c in s:
            if c.isalnum():
                s_up += c.lower()
        return s_up == s_up[::-1]
