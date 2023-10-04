class Solution:
    def compress(self, chars: list[str]) -> int:
        count = 1
        for i in range(len(chars) - 2, -2, -1):
            if i < 0 or chars[i] != chars[i + 1]:
                if count > 1:
                    for j, n in enumerate(str(count), start=i + 2):
                        chars[j] = n
                    j += 1
                    while j < len(chars) and chars[i + 1] == chars[j]:
                        chars.pop(j)
                count = 0
            count += 1
        return len(chars)
