"""
Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами.
Если это возможно, выведите строку YES, иначе выведите строку NO.

Треугольник — это три точки, не лежащие на одной прямой.
"""


def solution(triangle: list[int]):
    triangle.sort(reverse=True)

    if triangle[0] < triangle[1] + triangle[2]:
        return "YES"
    return "NO"


a = int(input())
b = int(input())
c = int(input())

print(solution([a, b, c]))
