class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            # even numbers in the binary system always end in 0, and odd in 1
            if n % 2:  # if number is odd, it ends in 1, so we increment count
                count += 1
            n = n >> 1  # then do right shift and check next bit
        return count


s = Solution()
print(s.hammingWeight(0b00000000000000000000000010000000))
print(s.hammingWeight(0b00000000000000000000000000001011))
print(s.hammingWeight(0b11111111111111111111111111111101))
