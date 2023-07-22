def find_max_symbol1(s: str) -> str:
    """O(k+n+k) = O(n)"""
    dct_chars = dict.fromkeys(set(s), 0)  # O(k)
    for char in s:  # O(n) - first time
        dct_chars[char] += 1

    # lambda variants
    return max(dct_chars, key=lambda x: dct_chars.__getitem__(x))  # O(n)
    return max(dct_chars.items(), key=lambda x: x[1])[0]  # O(n)


def find_max_symbol2(s: str) -> str:
    """O(k+n) = O(n)"""
    dct_chars = dict.fromkeys(set(s), 0)  # O(k)
    max_char = s[0]
    max_count = 0
    for char in s:  # O(n) - first time
        dct_chars[char] += 1
        if dct_chars[char] > max_count:
            max_count = dct_chars[char]
            max_char = char

    return max_char


def find_max_symbol(s: str) -> str:
    if s == "":
        return s
    return find_max_symbol1(s)
    return find_max_symbol2(s)


print(find_max_symbol("3aaa7bbbbbbb4ccc"))
print(find_max_symbol(""))
