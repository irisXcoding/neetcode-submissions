class TimeMap:

    def __init__(self):
        self.time_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.time_dict.get(key):
            self.time_dict[key].append((value, timestamp))
        else:
            self.time_dict[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        status = ""
        time_list = self.time_dict.get(key, [])
        left, right = 0, len(time_list)-1
        while left<=right:
            mid = (left+right)//2
            if time_list[mid][1] == timestamp:
                return time_list[mid][0]
            elif time_list[mid][1] < timestamp:
                left = mid+1
                status = time_list[mid][0]
            else:
                right = mid-1
        return status

