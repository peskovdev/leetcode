class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hashmap: dict[int, int] = {}
        res = 0
        for n in nums:
            if n in hashmap:
                res += hashmap[n]
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        return res
