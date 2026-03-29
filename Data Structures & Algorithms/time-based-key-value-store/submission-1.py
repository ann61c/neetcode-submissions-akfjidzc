class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = self.store.get(key, [])
        if not res:
            return ""
        left = 0
        right = len(res) - 1
        ans = ""
        while left <= right:
            mid = left + (right - left)//2
            if res[mid][1]<= timestamp:
                left = mid + 1
                ans = res[mid][0] 
            elif res[mid][1]>timestamp:
                right = mid - 1
            
        return ans

        
