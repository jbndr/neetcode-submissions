class TimeMap:

    def __init__(self):
        self.kv = {}
        self.timestamps = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kv:
            self.kv[key].append(value)
            self.timestamps[key].append(timestamp)
        else:
            self.kv[key] = [value]
            self.timestamps[key] = [timestamp]
        

    def get(self, key: str, timestamp: int) -> str:
        left = 0

        if key not in self.timestamps:
            # key has never been set
            return ""

        right = len(self.timestamps[key])

        while left < right:
            mid = (left+right) // 2

            if self.timestamps[key][mid] > timestamp:
                right = mid
            else:
                left = mid + 1

        if left - 1 >= 0 and left - 1 <= len(self.timestamps[key]):
            return self.kv[key][left-1]
        
        return ""


        
        
        

