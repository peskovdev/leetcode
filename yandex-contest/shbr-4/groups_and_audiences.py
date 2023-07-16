"""
В университете есть n аудиторий и m учебных групп.
Для каждой аудитории задана её вместимость, а для каждой группы — численность.
Группа может заниматься в аудитории только если её численность не превосходит размера аудитории.
Определите максимальное количество групп, которые можно рассадить по аудиториям.
"""


def solution(groups: list[int], room_num: int, rooms: list[int]) -> int:
    groups = sorted(groups, reverse=True)
    rooms = sorted(rooms, reverse=True)
    skipped_room = 0
    resolved = 0
    for group_len in groups:
        if skipped_room >= room_num:
            break
        if group_len <= rooms[skipped_room]:
            resolved += 1
            skipped_room += 1

    return resolved


def input_solution():
    _ = int(input())
    groups = [int(x) for x in input().split()]
    room_num = int(input())
    rooms = [int(x) for x in input().split()]
    result = solution(groups, room_num, rooms)
    print(result)


# input_solution()


assert solution(groups=[3, 3, 3, 1, 2], room_num=2, rooms=[1, 1]) == 1
assert solution(groups=[1, 2], room_num=3, rooms=[3, 2, 1]) == 2


def long_test():
    import random
    import time

    start_time = time.time()
    range_len = 100000
    print("long test started")
    random_groups = [random.randint(1, 10000) for _ in range(range_len)]
    random_rooms = [random.randint(1, 10000) for _ in range(range_len)]
    result = solution(random_groups, range_len, random_rooms)
    print("long test finished in:", time.time() - start_time)
    print("result = ", result)


long_test()
