# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return True


class Solution:
    def guessNumber(self, n: int) -> int:
        lp, rp = 1, n

        while lp <= rp:
            middle = (lp + rp) // 2

            target = guess(middle)
            if target < 0:
                rp = middle - 1
            elif target > 0:
                lp = middle + 1
            else:
                return middle
        return -1
