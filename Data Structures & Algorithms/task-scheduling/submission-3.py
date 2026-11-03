class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        ready = []
        pending = deque([])
        for k, v in task_count.items():
            heapq.heappush(ready, (-v,k))
        ts = 0
        while ready or pending:
            # check pending
            if pending and pending[0][1]==ts:
                item = pending.popleft()
                if item[-1]<0:
                    heapq.heappush(ready, (item[-1], item[0]))
            # get item from ready
            if ready:
                ready_item = heapq.heappop(ready)
                if (ready_item[0]+1)<0:
                    pending.append((ready_item[1], ts+n+1, ready_item[0]+1))
            ts+=1
        return ts