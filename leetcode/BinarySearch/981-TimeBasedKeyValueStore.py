class TimeMap:

    def __init__(self):
        self.arr = {} # key: List of [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.arr:
            self.arr[key] = []
        self.arr[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        row = self.arr.get(key, [])
        l = 0
        r = len(row) - 1

        while l <= r:
            m = (l + r) // 2

            if row[m][1] <= timestamp:
                res = row[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

#? Test Input
# ["TimeMap","set","get","get","set","get","get"]
# [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]


if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1)) # return "bar"
    print(timeMap.get("foo", 3)) # return "bar" since there is a value at timestamp 1 and 1 <= 3
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4)) # return "bar2"
    print(timeMap.get("foo", 5)) # return "bar2"
