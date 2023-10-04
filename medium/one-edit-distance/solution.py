class Solution:
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or s[i+1:] == t[i:] or s[i:] == t[i+1:]
        return True
