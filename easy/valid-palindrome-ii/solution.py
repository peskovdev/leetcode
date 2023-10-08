class Solution:
    def validPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1

        while lp < rp:
            if s[lp] != s[rp]:
                return (
                    s[lp + 1: rp + 1] == s[rp:lp:-1]
                    or s[lp:rp] == s[rp - 1: lp - 1: -1]
                    or s[lp:rp] == s[rp - 1:: -1]
                )
            lp += 1
            rp -= 1

        return True
