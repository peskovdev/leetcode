class Solution:
    def compress(self, chars: list[str]) -> int:
        count = 1
        for i in range(len(chars) - 2, -2, -1):
            if i < 0 or chars[i] != chars[i + 1]:
                if count > 1:
                    for j, n in enumerate(str(count), start=i + 2):
                        chars[j] = n
                    last = j + 1
                    while last < len(chars) and chars[i + 1] == chars[last]:
                        last += 1
                    for j in range(last - 1, j, - 1):
                        chars.pop(j)
                count = 0
            count += 1
        return len(chars)
