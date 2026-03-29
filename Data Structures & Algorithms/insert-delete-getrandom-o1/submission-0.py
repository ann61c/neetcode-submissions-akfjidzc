class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.data_map:
            self.data.append(val)
            self.data_map[val] = len(self.data) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data_map:
            index = self.data_map[val]
            last_index = len(self.data) - 1
            last_val = self.data[-1]

            self.data[index] = last_val
            self.data_map[last_val] = index

            self.data.pop()
            del self.data_map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()