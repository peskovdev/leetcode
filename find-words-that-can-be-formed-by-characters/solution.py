from string import ascii_lowercase


class Solution(object):
    def countCharacters(self, words, chars):
        dict_char = dict.fromkeys(ascii_lowercase, 0)
        for char in set(chars):
            dict_char[char] = chars.count(char)

        final_count = 0
        for word in words:
            fails = 0
            for char in set(word):
                if word.count(char) > dict_char[char]:
                    fails += 1
            if fails == 0:
                final_count += len(word)

        return final_count
