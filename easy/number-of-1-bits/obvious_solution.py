class Solution:
    def hammingWeight(self, n: int) -> int:
        s = f"{n:0b}"
        return len(s.replace("0", ""))


s = Solution()
print(s.hammingWeight(0b00000000000000000000000010000000))
print(s.hammingWeight(0b00000000000000000000000000001011))
print(s.hammingWeight(0b11111111111111111111111111111101))
