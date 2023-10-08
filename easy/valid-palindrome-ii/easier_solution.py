class Solution:
    def validPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1

        while lp < rp:
            if s[lp] != s[rp]:
                del_left, del_right = s[lp + 1: rp + 1], s[lp: rp]
                return del_left == del_left[::-1] or del_right == del_right[::-1]
            lp, rp = lp + 1, rp - 1

        return True
