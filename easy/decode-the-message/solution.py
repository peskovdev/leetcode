from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        table = {" ": " "}
        counter = 0
        for i, char in enumerate(key.replace(" ", "")):
            if char not in table:
                table[char] = ascii_lowercase[counter]
                counter += 1

        decoded_msg = "".join(table[char] for char in message)
        return decoded_msg


o = Solution()
print(
    o.decodeMessage(
        "the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"
    )
)
print(
    o.decodeMessage(
        "eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
    )
)
