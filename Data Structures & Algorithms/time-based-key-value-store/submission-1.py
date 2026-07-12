from collections import defaultdict 

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list) 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))  
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        l = 0
        r = len(self.time_map[key]) - 1  
        result = ""
        
        while l <= r: 
            mid = (l + r) // 2

            if self.time_map[key][mid][0] <= timestamp:
                result = self.time_map[key][mid][1] 
                l = mid + 1 

            else:
                r = mid - 1

        return result 


        
        
