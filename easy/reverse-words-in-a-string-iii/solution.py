class Solution:
    def reverseWords(self, s: str) -> str:
        res = list(s)
        lp, rp = 0, 0
        while rp < len(res):
            while (rp + 1) < len(res) and res[rp + 1] != " ":
                rp += 1
            next_pointer = rp + 2

            while lp < rp:
                res[lp], res[rp] = res[rp], res[lp]
                lp, rp = lp + 1, rp - 1
            lp = rp = next_pointer
        return "".join(res)
