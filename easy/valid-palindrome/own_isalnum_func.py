class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1

        while lp < rp:
            if not self.is_alnum(s[lp]):
                lp += 1
                continue
            if not self.is_alnum(s[rp]):
                rp -= 1
                continue
            if s[lp].lower() != s[rp].lower():
                return False
            lp += 1
            rp -= 1

        return True

    def is_alnum(self, c: str) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
