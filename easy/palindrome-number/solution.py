class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = []
        while x != 0:
            res.append(x % 10)
            x = x // 10

        return res == res[::-1]
