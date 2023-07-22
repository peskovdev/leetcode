"""
Решите в целых числах уравнение:
    sqrt(ax+b) = c
    sqrt(ax+b) = c
    a, b, c – данные целые числа: найдите все решения или сообщите, что решений в целых числах нет.
"""


def solution(a, b, c):
    if a == 0:
        if b == c ** 2:
            return "MANY SOLUTIONS"
        else:
            return "NO SOLUTION"
    x = (c**2 - b) / a
    if x != int(x):
        return "NO SOLUTION"
    return int(x)


# a = int(input())
# b = int(input())
# c = int(input())
# print(solution(a, b, c))


print(solution(1, 0, 0))
print(solution(1, 2, 3))
print(solution(1, 2, -3))
