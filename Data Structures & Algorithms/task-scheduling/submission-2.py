from collections import deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # (-count, task_name)
        ready = []
        # (-count, task_name, next_ready_time)
        cooling = deque([])
        count_dict = {}
        for task in tasks:
            count_dict[task] = count_dict.get(task, 0) + 1
        
        for k, v in count_dict.items():
            heapq.heappush(ready, (-v, k))
        ts = 0
        while ready or cooling:
            if cooling and cooling[0][2] == ts:
                cooling_item = cooling.popleft()
                heapq.heappush(ready, (cooling_item[0], cooling_item[1]))
            if ready:
                item = heapq.heappop(ready)
                if -item[0] != 1:
                    cooling.append([item[0] + 1, item[1], ts + n + 1])
            ts += 1
        return ts
