class Solution:
    def isValid(self, s: str) -> bool:
        skobki_counter = []

        for skobka in s:
            if skobka == "{" or skobka == "[" or skobka == "(":
                skobki_counter.append(skobka)
                continue
            if len(skobki_counter) == 0:
                print(skobki_counter)
                return False
            if skobka == "}":
                if skobki_counter[-1] != "{":
                    return False
            elif skobka == "]":
                if skobki_counter[-1] != "[":
                    return False
            elif skobka == ")":
                if skobki_counter[-1] != "(":
                    return False
            skobki_counter.pop()
        return len(skobki_counter) == 0
