from collections import deque
import heapq
from typing import Counter


def leastInterval(tasks, n):

    count = Counter(tasks)
    maxHeap = [-c for c in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()

    while maxHeap or q:
        time += 1
        if maxHeap:
            count = 1 + heapq.heappop(maxHeap)
            if count:
                q.append([count, time + n])
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])

    return time

    # task_count = {}
    # task_wait = []
    # for t in tasks:
    #     if t not in task_count:
    #         task_wait.append((0,t))
    #     task_count[t] = task_count.get(t, 0) + 1
    #
    #
    # intervals = 0
    # heapq.heapify(task_wait)
    #
    # while task_count:
    #     t = heapq.heappop(task_wait)
    #     task = t[1]
    #     turns = t[0]
    #
    #
    #     if turns != 0:
    #         intervals += 1
    #         continue
    #
    #     task_count[task] -= 1
    #     intervals += 1
    #     heapq.heappush(task_wait, (n, task))
    #     if task_count[task] == 0:
    #         task_count.pop(task)
    #
    # return intervals
