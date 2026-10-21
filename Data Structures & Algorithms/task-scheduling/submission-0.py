import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        copies = {}
        for task in tasks:
            copies[task] = copies.get(task, 0)+1
        ready_hq = []
        heapq.heapify(ready_hq)
        for k, v in copies.items():
            heapq.heappush(ready_hq, (-v, k)) # max heap
        cycle_count = 0
        cooling = deque([])
        while ready_hq or cooling:
            cycle_count+=1
            # run task
            if ready_hq:
                cur_task = heapq.heappop(ready_hq)
                remain = cur_task[0]+1
                if remain<0:
                    deque.append(cooling, (remain, cur_task[1], cycle_count+n))
            # release task
            if cooling and cooling[0][2]==cycle_count:
                    ready_item = deque.popleft(cooling)
                    heapq.heappush(ready_hq, (ready_item[0], ready_item[1]))
        return cycle_count
