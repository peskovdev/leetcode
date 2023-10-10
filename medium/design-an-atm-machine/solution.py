class ATM:
    def __init__(self):
        self.banknotes = [[20, 0], [50, 0], [100, 0], [200, 0], [500, 0]]

    def deposit(self, banknotesCount: list[int]) -> None:
        for i in range(len(self.banknotes)):
            self.banknotes[i][1] += banknotesCount[i]

    def withdraw(self, amount: int) -> list[int]:
        res = [0, 0, 0, 0, 0]

        for i in range(len(self.banknotes) - 1, -1, -1):
            nominal, quantity = self.banknotes[i]
            if amount >= nominal:
                res[i] = min(amount // nominal, quantity)
                amount -= nominal * res[i]

        if amount:
            return [-1]

        for i in range(len(self.banknotes)):
            self.banknotes[i][1] -= res[i]
        return res
