class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_position = sorted(zip(position, speed), key=lambda a:a[0])
        max_time = 0
        final_count = 0
        for idx in range(len(sorted_position)-1, -1, -1):
            pos, spd = sorted_position[idx]
            _time = (target-pos)/spd
            if _time > max_time:
                max_time = _time
                final_count += 1
        return final_count

        