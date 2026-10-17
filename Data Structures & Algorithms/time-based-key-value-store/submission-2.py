class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        target_values = self.timemap[key]
        l, r = 0, len(target_values) - 1
        result_idx = float("-inf")
        time_stamp_prev = float("-inf")
        while l <= r:
            mid = (l + r) // 2
            if target_values[mid][1] == timestamp:
                result_idx = mid
                break
            elif target_values[mid][1] > timestamp:
                r = mid - 1
            else:
                if target_values[mid][1] >= time_stamp_prev:

                    time_stamp_prev = target_values[mid][1]
                    result_idx = mid

                l = mid + 1
        
        return target_values[result_idx][0] if result_idx != float("-inf") else ""

        
