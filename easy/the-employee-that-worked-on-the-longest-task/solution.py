class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        workers: dict[int, int] = {}
        start_time = 0
        for log in logs:
            task_time = log[1] - start_time
            if not workers.get(log[0]) or workers[log[0]] < task_time:
                workers[log[0]] = log[1] - start_time
            start_time = log[1]

        print(workers)
        return max(workers, key=lambda x: (workers[x], -x))


sol = Solution()
print(sol.hardestWorker(10, [[0, 3], [2, 5], [0, 9], [1, 15]]))
print(sol.hardestWorker(10, [[1, 1], [3, 7], [2, 12], [7, 17]]))
print(sol.hardestWorker(10, [[0, 10], [1, 20]]))
print(
    sol.hardestWorker(
        10, [[4, 1], [0, 2], [1, 3], [15, 4], [2, 10], [15, 16], [5, 20]]
    )
)
print(
    sol.hardestWorker(
        10,
        [
            [110, 5],
            [360, 7],
            [48, 8],
            [286, 10],
            [167, 12],
            [110, 13],
            [221, 18],
        ],
    )
)
