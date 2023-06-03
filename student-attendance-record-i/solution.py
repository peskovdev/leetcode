class Solution(object):
    def checkRecord(self, s):
        if s.count("A") >= 2 or "LLL" in s:
            return False
        return True
