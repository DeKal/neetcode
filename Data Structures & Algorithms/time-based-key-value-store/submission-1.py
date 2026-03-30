class TimeMap:

    def __init__(self):
        self.time_dict = {}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = []

        self.time_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_dict:
            return ""
        
        timestamps = self.time_dict[key]
        # 2
        #1 3 5
        l = 0
        r = len(timestamps)-1
        while l <= r:
            m = l + (r-l)//2

            mid_ts, value = timestamps[m]
            if timestamp == mid_ts:
                return value
            elif timestamp > mid_ts:
                l = m+1
            elif timestamp < mid_ts:
                r = m-1
        
        return timestamps[r][1] if timestamp > timestamps[r][0]  else ""


        
        

