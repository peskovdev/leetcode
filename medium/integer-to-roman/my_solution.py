class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {
            1: {"one": "I", "five": "V"},
            2: {"one": "X", "five": "L"},
            3: {"one": "C", "five": "D"},
            4: {"one": "M"},
        }
        actions = {
            "1": ["one"],
            "2": ["one", "one"],
            "3": ["one", "one", "one"],
            "4": ["one", "five"],
            "5": ["five"],
            "6": ["five", "one"],
            "7": ["five", "one", "one"],
            "8": ["five", "one", "one", "one"],
            "9": ["nine"],
        }

        grade = len(str(num))
        res = []
        for n in str(num):
            if n != "0":
                char = []
                symbols = actions[n]
                for symbol in symbols:
                    if symbol == "nine":
                        char.append(hashmap[grade]["one"])
                        char.append(hashmap[grade + 1]["one"])
                    else:
                        char.append(hashmap[grade][symbol])
                res.append("".join(char))
            grade -= 1
        return "".join(res)
