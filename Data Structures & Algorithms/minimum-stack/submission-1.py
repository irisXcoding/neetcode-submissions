class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            cur_min = val
        else:
            last_min = self.stack[-1][1]
            cur_min = min(val, last_min)
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
